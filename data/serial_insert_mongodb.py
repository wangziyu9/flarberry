import serial
import pymongo
import time

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.rpi
collection_HT = db.HT
collection_WL = db.WL
collection_EH = db.EH


ser = serial.Serial("/dev/ttyUSB0",9600)
line = ser.readline() 

def write_TH(line):
    ht = {}
    ht['time'] = time.time()
    ht['humidity'] = float(line.split(' ')[1])
    ht['temperature'] = float(line.split(' ')[3])
    collection_HT.insert_one(ht)
    pass

def write_WL(line):
    wl = {}
    wl['time'] = time.time()
    wl['water_level'] = float(line.split(' ')[1])
    collection_WL.insert_one(wl)
    pass

def write_EH(line):
    eh = {}
    eh['time'] = time.time()
    if line.split(' ')[1] == "inf":
        eh['earth_humidity'] = 100000
    else:
        eh['earth_humidity'] = float(line.split(' ')[1])
    collection_EH.insert_one(eh)
    pass

while line: 
    line = str(ser.readline())
    print(line)
    if('Humidity' in line):
        write_TH(line)
    if('Water_level' in line):
        write_WL(line)
    if('Earth_humidity' in line):
        write_EH(line)
    else:
        pass
        
    print(line)
