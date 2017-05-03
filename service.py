from flask import Flask
from flask import jsonify
from flask import request,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
#import predict

app = Flask(__name__)
#global pred_object
#pred_object = None

app.config['MONGO_DBNAME'] = 'predict'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/predict'

mongo = PyMongo(app)

@app.route('/')
def todo():
    print "################In root"
    return render_template('index.html')

@app.route('/api/getPrediction', methods=['POST'])
def add_star():
    print "################In Post"
    task = request.json['text']
#    result_summary =  pred_summary.get_prediction(task)
#    print result_summary

#    result_praise = pred_praise.get_prediction(task)
#    print result_praise

#    result_problem = pred_problem.get_prediction(task)
#    print result_problem

#    result_solution = pred_solution.get_prediction(task)
#    print result_solution

#   result_localization = pred_localization.get_prediction(task)
#    print result_localization

#    result_neutrality = pred_neutrality.get_prediction(task)
#    print result_neutrality

#    result_mitigation = pred_mitigation.get_prediction(task)
#    print result_mitigation
    return jsonify({'result' :{'summary' : 'Positive','praise' : 'Negative','problem':'Positive','solution':'Negative','localization':'Positive','neutrality':'Negative','mitigation':'Positive'}})
#    return jsonify({'result' : {'summary' : result_summary,'praise' : result_praise,'problem' : result_problem,'solution' : result_solution,'localization' : result_localization,'neutrality' : result_neutrality,'mitigation' : result_mitigation}})


@app.route('/api/postPrediction',methods=['POST'])
def add_pred():
    task = request.get_json(silent=True)
    pred = mongo.db.predict
    pred_id = pred.insert({'comment':task['comment'],'pred': task['fields']})
    new_pred = pred.find_one({'_id': pred_id })
    output = {'_id':str(pred_id),'task' : task['fields']}
    return jsonify({'result' : output})
    
def main():
    print "################In main"
#    global pred_summary
#    pred_summary = predict.Prediction(suffix='Summary')
#    global pred_praise
#    pred_praise = predict.Prediction(suffix='Praise')
#    global pred_problem
#    pred_problem = predict.Prediction(suffix='Problem')
#    global pred_solution
#    pred_solution = predict.Prediction(suffix='Solution')
#    global pred_mitigation
#    pred_mitigation = predict.Prediction(suffix='Mitigation')
#    global pred_neutrality
#    pred_neutrality = predict.Prediction(suffix='Neutrality')
#    global pred_localization
#    pred_localization = predict.Prediction(suffix='Localization')
    app.run(host='0.0.0.0', debug=True,use_reloader=False, port=5001)


if __name__ == '__main__':
    main()
