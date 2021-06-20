from flask import Flask
from flask import render_template
import pymongo
from bson.json_util import dumps


app = Flask(__name__)


# myclient = pymongo.MongoClient(
#     "mongodb://fre:frezer@cluster0-shard-00-00.7xkdf.mongodb.net:27017,cluster0-shard-00-01.7xkdf.mongodb.net:27017,cluster0-shard-00-02.7xkdf.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-11kjk0-shard-0&authSource=admin&retryWrites=true&w=majority")
# mydb = myclient["mydatabase"]
# mycol = mydb["News"]
# mycolAbiy = mydb["abiyahmadali"]
# mycolTikvah = mydb["tikvah"]
# mycolBisrat = mydb["BisratSport"]
# mycolEbc = mydb["ebc"]


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/api")
def hello_world():
    return "Hello Mitu"

@app.route('/news', methods=['GET'])
def get_all_stars():
    return dumps(list(mycol.find().limit(50)), indent=2)


@app.route('/news/telegram/tikvah', methods=['GET'])
def get_all_telegram_tikvah():
    return dumps(list(mycolTikvah.find().limit(20)), indent=2)


@app.route('/news/telegram/ebc', methods=['GET'])
def get_all_telegram_ebc():
    return dumps(list(mycolEbc.find().limit(20)), indent=2)


@app.route('/news/telegram/bisratsport', methods=['GET'])
def get_all_telegram_bisratsport():
    return dumps(list(mycolBisrat.find().limit(20)), indent=2)


@app.route('/news/twitter/abiyahmadali', methods=['GET'])
def get_all_twitter():
    return dumps(list(mycolAbiy.find().limit(20)), indent=2)

