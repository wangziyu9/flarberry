# encoding:utf-8
import time
from flask import Flask,render_template,request,jsonify

import config_json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("HTW_charts.html")

@app.route('/data', methods=['GET', 'POST'])
def rtn_data():
    d = config_json.get_data()
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)