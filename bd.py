# 2017 github:/nehsus
#test with exo.csv in "input"
from flask import Flask, render_template, request, send_file, redirect, url_for, make_response
from datetime import datetime
from flask import jsonify
import json, ast
import numpy as np
import csv
import os
from pymongo import MongoClient
from werkzeug import secure_filename
from sm import parseAndWrite, preProcess
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
client = MongoClient("localhost", 27017)

def plsJson(xlol):
    st=[]
    for i in xlol:
        del i["_id"]
        st.append(i)
    bun= ast.literal_eval(json.dumps(st))
    finalbun= str(bun).replace("'", "\"")
    return finalbun

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/plot.png')
def plot():
    figgy = exo()
    img = StringIO()
    figgy.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    response='notOK'
    if request.method == 'POST':
        file=request.files['file']
        if file:
            print ("OK GReat")
            filename= secure_filename(file.filename)
            file.save(filename)
            return render_template("index.html")
        else:
            return redirect(url_for('index'))

@app.route('/data')
def data():
    dat= client["pene"].things.find()
    return plsJson(dat)

#rtype {"name": "bun"}

if __name__ == "__main__":
    print("\n Established at :27017 \n")
    app.run(debug=True)


