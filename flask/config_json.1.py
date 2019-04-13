import pymongo
import time
import config_date

client = pymongo.MongoClient(host='10.84.126.18', port=27017)
db = client.rpi
collection_HT = db.HT
collection_WL = db.WL
collection_EH = db.EH

humidity = []
temperature = []
water_lever = []
earth_humidity = []

data = {}

data['humidity'] = humidity
data['temperature'] = temperature
data['water_lever'] = water_lever
data['earth_humidity'] = earth_humidity

def get_data():
    dhts = collection_HT.find().limit(12)
    dwls = collection_WL.find().limit(12)
    dehs = collection_EH.find().limit(12)
    
    for d in dhts:
        humidity.append(d['humidity'])
        temperature.append(d['temperature'])

    for d in dwls:
        # print(d)
        water_lever.append(d['water_level'])
        # 这里键错了，日后修正过来。已修正
    
    for d in dehs:
        earth_humidity.append(d['earth_humidity'])

    return(data)
    
def get_data_by_time():


if __name__ == "__main__":
    print(get_data())