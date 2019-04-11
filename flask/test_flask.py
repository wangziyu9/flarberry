# encoding:utf-8

import time

from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("test.html")

@app.route('/color', methods=['GET', 'POST'])
def pst():
    if request.method == 'POST':
        values = request.values.get("color", 0)

        return "post baka" + values
    else:
        return "not post"

@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0')