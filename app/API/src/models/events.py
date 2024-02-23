from pydantic import BaseModel, Field
from typing import Optional, Union, Annotated
from datetime import date, time, datetime
from enum import Enum


class EventCreate(BaseModel):
    """Create a new event"""
    
    id: int
    event_date: datetime
    attribute1: Optional[int] = None
    attribute2: Optional[int] = None
    attribute3: Optional[int] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[bool] = None
    metric1: int
    metric2: float

    class Config:
        orm_mode = True


class EventRead(BaseModel):
    id: Optional[int] = None
    event_date: Optional[datetime] = None
    attribute1: Optional[int] = None
    attribute2: Optional[int] = None
    attribute3: Optional[int] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[bool] = None
    metric1: Optional[int] = None
    metric2: Optional[float] = None

    class Config:
        orm_mode = True

class QueryFilterRestr(BaseModel):
    filter_attr: Optional[str] = None
    filter_val: Optional[str] = None
    
    class Config:
        orm_mode = True

#class AttrRestrGranularity(Enum):
#    HOURLY = "hourly"
#    DAILY = "daily"
#class AttrRestrMetrics(Enum):
#    METRIC1 = "metric1"
#    METRIC2 = "metric2"
#    
#    def form_regexp(self):
#        return f"^{self.METRIC1}$|^{self.METRIC2}$|^{self.METRIC1},{self.METRIC2}$"
#
#class AnalyticsQuery(BaseModel):
#    groupBy: str
#    metrics: AttrRestrMetrics
#    filters: Optional[dict] = None
#    granularity: AttrRestrGranularity
#    startDate: Optional[datetime] = datetime.combine(datetime.now(), time.min)
#    endDate: Optional[datetime] = datetime.now().replace(microsecond=0)
