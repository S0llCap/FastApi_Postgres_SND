from datetime import date, time, datetime

def QueryForEventAnalytics(groupBy: str, metrics: str, granularity: str,
                            startDate: datetime, endDate: datetime, filter_attr: str = None, filter_val: str = None):
    
    agg_list = ""
    for field in metrics.split(","):
        agg_list += f"sum({field}) as {field},"
    agg_list = agg_list[:len(agg_list)-1]
    
    agg_dt = ""
    if granularity == 'hourly':
        agg_dt = "date_trunc('hour', event_date + event_time)"
    else:
        agg_dt = "event_date"
    
    query_select = f"select {groupBy}, {agg_dt} as event_date, {agg_list} from adv_data.events"
    
    filters_list = f"and event_date >= '{startDate.date()}' and event_date + event_time >= '{startDate}'"
    filters_list += f" and event_date < '{endDate.date()}' and event_date + event_time < '{endDate}'"
    if filter_attr:
        for (flt, val) in zip(filter_attr.split(","), filter_val.split(",")):
            filters_list += f" and {flt} = {val}"
        
    query_where = f"where 1=1 {filters_list}"
    query_group = f"group by {groupBy}, {agg_dt}"
    db_query = ' '.join([query_select, query_where, query_group])
    
    return db_query
        
