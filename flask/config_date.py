import pymongo
import time

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY 
MONTH = 30 * DAY

def get_time_date():
    time_data = {}
    time_str = []
    time_stamp_list = [(time.time() - MINUTE * x) for x in range(12)]
    for t in time_stamp_list:
        time_str.append(time.localtime(t).tm_hour + time.localtime(t).tm_min)

    time_data['time_str'] = time_str
    time_data['time_stamp'] = time_stamp_list
    return(time_data)