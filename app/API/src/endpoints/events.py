from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Union, Annotated
from models.events import EventCreate, EventRead, QueryFilterRestr #,AnalyticsQuery, AttrRestrMetrics, AttrRestrGranularity, 
from psycopg.rows import class_row
from datetime import time, datetime
from db.db_setup import get_pool
from endpoints.events_funchelp import QueryForEventAnalytics


tags_metadata = [
    {
        "name": "EventAdd",
        "description": "Add an event",
    },
    {
        "name": "EventGetAggData",
        "description": "Get analytics data for events",
    }
]


router = APIRouter()
pool = get_pool()

@router.post("/event", tags=['EventAdd'])
def addEvent(event_create: EventCreate):
    query_params = event_create.__dict__
    with pool.connection() as conn:
        conn.execute(
            """insert into adv_data.Events 
            values (%(id)s, %(event_date)s::date, %(event_date)s::time, 
            %(attribute1)s, %(attribute2)s, %(attribute3)s, %(attribute4)s, %(attribute5)s, %(attribute6)s, 
            %(metric1)s, %(metric2)s)""",
            query_params)

@router.get("/analytics/query", response_model=List[EventRead], response_model_exclude_unset=True, tags=['EventGetAggData'])
def getAnalyticsData(groupBy: Annotated[str, Query(description="Attributes for grouping (comma-separated)")],
                    metrics: Annotated[str, Query(pattern='^metric1$|^metric2$|^metric1,metric2$|^metric2,metric1$', description="Metrics to retrieve (comma-separated, always sums)")],
                    granularity: Annotated[str, Query(pattern='^hourly$|^daily$', description="Granularity (hourly or daily)")],
                    filters: Annotated[Union[List[str], None], Depends(QueryFilterRestr)] = None,
                    startDate: Annotated[Union[datetime, None], Query(description="Start date and time for filtering (format: YYYY-MM-DDTHH:mm:ss)")] = datetime.combine(datetime.now(), time.min),
                    endDate: Annotated[Union[datetime, None], Query(description="End date and time for filtering (format: YYYY-MM-DDTHH:mm:ss)")] = datetime.now().replace(microsecond=0)
                    ):
    if filters.filter_attr and len(filters.filter_attr.split(",")) != len(filters.filter_val.split(",")):
        raise HTTPException(status_code=400, detail="Bad Request: the number of attributes does not match the number of values.")
    
    result = []
    with pool.connection() as conn, conn.cursor(row_factory=class_row(EventRead)) as cur:
        db_query = QueryForEventAnalytics(groupBy, metrics, granularity, startDate, endDate, filters.filter_attr, filters.filter_val)
        #print(db_query)
        result = cur.execute(db_query).fetchall()
        
    return result
