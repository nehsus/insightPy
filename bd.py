# 2017 github:/nehsus
#test with Suicides.csv in "input"
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pymongo import MongoClient
from flask import jsonify
import json, ast
import numpy as np
import pandas as pandu
import csv
import os
from werkzeug import secure_filename
from sm import parseAndWrite, suisight

app = Flask(__name__)
client = MongoClient("localhost", 27017)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    response='notOK'
    if request.method == 'POST':
        file=request.files['file']
        if file:
            print ("OK GReat")
            filename= secure_filename(file.filename)
            file.save(filename)
            
            dbNOW= client['pene']
            #select current db name
            #current collection name
            colNOW= 'things'
            db=dbNOW[colNOW]
            db.drop()
            parseAndWrite(db, filename)
            
            return render_template("index.html")

        else:
            return redirect(url_for('index'))

@app.route('/data')
def data():
    st1=[]
    dat= client["pene"].things.find()
    for i in dat:
        #passes json from pene database into js removes bloat
        del i["_id"]
        st1.append(i)
    bast = ast.literal_eval(json.dumps(st1))
    finalJSON = str(bast).replace("'", "\"")
    return finalJSON
#rtype {"name": "BT"}
 #Parse uploaded CSV using pandas and pymongo to db


if __name__ == "__main__":
    print("\n Established at :27017 \n")
    app.run(debug=True)


