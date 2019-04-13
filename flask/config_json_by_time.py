import pymongo
import time
import config_date

client = pymongo.MongoClient(host='10.84.126.18', port=27017)
db = client.rpi
collection_HT = db.HT
collection_WL = db.WL
collection_EH = db.EH

time_date = config_date.get_time_date()

def find_data():
    db.HT.find({"time":{'$gt' : 1554987589.2462833}}).sort([("time",1)]).limit(1)
    pass


def get_data():
    humidity = []
    temperature = []
    water_lever = []
    earth_humidity = []
    time_stamp = []

    # last 12 data
    dhts = collection_HT.find().sort([("time",-1)]).limit(12)
    dwls = collection_WL.find().sort([("time",-1)]).limit(12)
    dehs = collection_EH.find().sort([("time",-1)]).limit(12)
    
    for d in dhts:
        humidity.append(d['humidity'])
        temperature.append(d['temperature'])
        time_stamp.append(d['time'])
        # print(time.localtime(d['time']))

    for d in dwls:
        # print(d)
        water_lever.append(d['water_level'])
        # 这里键错了，日后修正过来。已修正
    
    for d in dehs:
        earth_humidity.append(d['earth_humidity'])

    data = {}
    data['humidity'] = humidity
    data['temperature'] = temperature
    data['water_lever'] = water_lever
    data['earth_humidity'] = earth_humidity
    data['time_stamp'] = time_stamp

    # time asc
    for key in data:
        data[key].reverse()
    print(data)
    return(data)
    
if __name__ == "__main__":
    print(get_data())