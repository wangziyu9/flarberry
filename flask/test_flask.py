# encoding:utf-8
import time
from flask import Flask,render_template,request,jsonify
# import ralay_switch
import config_json_by_time
import config_json
# from gpiozero import LED

app = Flask(__name__)
ralay_gpio = 24
ralay = 0

MINUTE = 60
HOUR = 60 * MINUTE
HOUR2 = HOUR * 2
DAY = 24 * HOUR
WEEK = 7 * DAY 
MONTH = 30 * DAY

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return render_template("HTW_charts.1.html")



@app.route('/data/minute', methods=['GET', 'POST'])
def rtn_data_by_minute():
    d = config_json_by_time.get_data_by_time_list(MINUTE)
    print(d)
    return jsonify(d)
@app.route('/data/hour', methods=['GET', 'POST'])
def rtn_data_by_hour():
    d = config_json_by_time.get_data_by_time_list(HOUR)
    print(d)
    return jsonify(d)
@app.route('/data/day', methods=['GET', 'POST'])
def rtn_data_by_day():
    d = config_json_by_time.get_data_by_time_list(DAY)
    print(d)
    return jsonify(d)

@app.route('/data', methods=['GET', 'POST'])
def rtn_data():
    d = config_json_by_time.get_last_data()
=======
    return render_template("HTW_charts.html")

@app.route('/data', methods=['GET', 'POST'])
def rtn_data():
    # d = config_json.get_data()
    d = config_json_by_time.get_data_by_time_list(MINUTE)
>>>>>>> 9074a210041957080cca204d293ccf4c7ec9131c
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True) # debug = True)