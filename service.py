from flask import Flask
from flask import jsonify
from flask import request,render_template
from flask_pymongo import PyMongo
import argparse
from bson.objectid import ObjectId
import predict

app = Flask(__name__)
#global pred_object
#pred_object = None

app.config['MONGO_DBNAME'] = 'predict'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/predict'

mongo = PyMongo(app)

@app.route('/')
def root_index():
    print "Inside root"
    return render_template('index.html')

@app.route('/api/getPrediction', methods=['POST'])
def get_prediction():
    print "Inside Post"
    task = request.json['text']
    print task
    #return jsonify({'result': {'0': 'Positive', '1': 'Negative', '2': 'Positive', '3': 'Negative', '4': 'Positive',
    #                           '5': 'Negative', '6': 'Positive'}})    
    result_summary =  pred_summary.get_prediction(task)
    print result_summary

    result_praise = pred_praise.get_prediction(task)
    print result_praise

    result_problem = pred_problem.get_prediction(task)
    print result_problem

    result_solution = pred_solution.get_prediction(task)
    print result_solution

    result_localization = pred_localization.get_prediction(task)
    print result_localization

    result_neutrality = pred_neutrality.get_prediction(task)
    print result_neutrality

    result_mitigation = pred_mitigation.get_prediction(task)
    print result_mitigation
    return jsonify({'result' : {'0' : result_summary,'1' : result_praise,'2' : result_problem,'3' : result_solution,'4' : result_localization,'5' : result_neutrality,'6' : result_mitigation}})


#['Comments', 'Praise', 'Problem', 'Solution', 'Mitigation','Neutrality', 'Localization', 'Summary']
@app.route('/api/postPrediction',methods=['POST'])
def add_prediction():
    task = request.get_json(silent=True)
    print task['comment']['text']
    pred = mongo.db.predict
    pred_id = pred.insert({'Comments':task['comment']['text'],'Summary': int(task['fields']['0']),'Praise': int(task['fields']['1']),'Problem':int(task['fields']['2']),'Solution':int(task['fields']['3']),'Localization':int(task['fields']['4']),'Neutrality':int(task['fields']['5']),'Mitigation':int(task['fields']['6']),'trained':'false'})
    print "new row...",task['fields']
    new_pred = pred.find_one({'_id': pred_id })
    output = {'_id':str(pred_id),'task' : task['fields']}
    return jsonify({'result' : output})
    
def main():
    print "Inside service main"

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="increase output verbosity")
    args = parser.parse_args()
    hard_train = False
    if args.train == True:
        print "model will be trained"
        hard_train = True
    #app.run(host='0.0.0.0', debug=True, use_reloader=False, port=5001)
    global pred_summary
    pred_summary = predict.Prediction(suffix='Summary',hard_train=hard_train  )
    global pred_praise
    pred_praise = predict.Prediction(suffix='Praise',hard_train=hard_train)
    global pred_problem
    pred_problem = predict.Prediction(suffix='Problem',hard_train=hard_train)
    global pred_solution
    pred_solution = predict.Prediction(suffix='Solution',hard_train=hard_train)
    global pred_mitigation
    pred_mitigation = predict.Prediction(suffix='Mitigation',hard_train=hard_train)
    global pred_neutrality
    pred_neutrality = predict.Prediction(suffix='Neutrality',hard_train=hard_train)
    global pred_localization
    pred_localization = predict.Prediction(suffix='Localization',hard_train=hard_train)
    app.run(host='0.0.0.0', debug=True,use_reloader=False, port=5002)


if __name__ == '__main__':
    main()
