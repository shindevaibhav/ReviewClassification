from flask import Flask
from flask import jsonify
from flask import request,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import predict

app = Flask(__name__)

pred_object = None
@app.route('/')
def todo():
    return render_template('index.html')

@app.route('/api/getPrediction', methods=['POST'])
def add_star():
  task = request.json['text']
  print pred_object.get_prediction(task)
  return jsonify({'result' : predict.get_prediction(task)})

if __name__ == '__main__':
    global pred_object
    pred_object = predict.Prediction()
    app.run(host='0.0.0.0', debug=True,port=5001)

