from flask import Flask
from flask import jsonify
from flask import request,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import predict

app = Flask(__name__)
#global pred_object
#pred_object = None

@app.route('/')
def todo():
    print "################In root"
    return render_template('index.html')

@app.route('/api/getPrediction', methods=['POST'])
def add_star():
    print "################In Post"
    task = request.json['text']
    result =  pred_object.get_prediction(task)
    print result
    return jsonify({'result' : result})

if __name__ == '__main__':
    print "################In main"
    global pred_object
    pred_object = predict.Prediction()
    app.run(host='0.0.0.0', debug=True,port=5001)

