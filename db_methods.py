from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient()
db = client.predict
pred = db.predict

def find_new_reviews_db():
  data = pred.find({'trained':u'false'})
  for record in data:
    print record

def update_review_db(pred_id):
  #pred.find_one({'_id': ObjectId(pred_id)}).update({'trained':u'true'})  
  pred.update_one({
  '_id': ObjectId(pred_id)
  },{
  '$set': {
    'trained': u'true'
  }
  }, upsert=False)  


#findFalse()
#updateFalse("590f94d0dcb2c44938863908")
#findFalse()
