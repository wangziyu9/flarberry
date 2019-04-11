import pymongo
import time
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.tvs

condition = {'id':'20170103'}
tv = collection.find_one(condition)
tv['time'] = time.time()
result = collection.update_one(condition, {'$set' : tv})

result = collection.find_one({'id':'20170103'})
print(result['time'])