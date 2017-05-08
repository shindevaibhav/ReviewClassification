from bson.objectid import ObjectId
from pymongo import MongoClient
import pandas as pd
client = MongoClient()
db = client.predict
pred = db.predict

def find_new_reviews_db():
  data = pred.find({'trained':u'false'})
  #for record in data:
  #  print record
  df = pd.DataFrame(list(data))
  return df

def update_review_db(ids):
  for id in ids:
      pred.update_one({
      '_id': id
      },{
      '$set': {
        'trained': u'true'
      }
      }, upsert=False)


#findFalse()
#updateFalse("590f94d0dcb2c44938863908")
#findFalse()
