from flask import Flask
import pymongo
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/a')
def hello_a():
    return 'Hello, a!'

@app.route('/mongo')
def connect_mongo():

    client = pymongo.MongoClient("mongodb://root:example@mongo_1:27017")
    # db = client.test
    # collection_test = db.test
    mydb = client["test"]
    mycol = mydb["ttt"]
    # 插入資料
    simple_data = {"123": "456"}
    data_id = mycol.insert_one(simple_data).inserted_id

    return str(data_id)


app.run(host='0.0.0.0')