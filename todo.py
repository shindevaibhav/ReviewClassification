from flask import Flask
from flask import jsonify
from flask import request,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/')
def todo():
  return render_template('index.html')

@app.route('/api/getPrediction', methods=['POST'])
def add_star():
  task = request.json['text']
  print predict.get_prediction(task)
  return jsonify({'result' : predict.get_prediction(task)})

if __name__ == '__main__':
    import predict
    app.run(host='0.0.0.0', debug=True,port=5001)

