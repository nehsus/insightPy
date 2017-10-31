from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient
from flask import jsonify
import json, ast

app = Flask(__name__)
client = MongoClient("localhost", 27017)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/d")
def d():
    return request.body.args("name")

@app.route('/data')
def data():
    st1=[]
    dat= client["pene2"].test.find()
    for i in dat:
        #passes json from pene database into js removes bloat
        del i["_id"]
        st1.append(i)
    bast = ast.literal_eval(json.dumps(st1))
    finalJSON = str(bast).replace("'", "\"")
    return finalJSON
#rtype {"name": "BT"}

if __name__ == "__main__":
    print("\n\tConnected to Nehsuspace:27017\n\n")
    app.run()


