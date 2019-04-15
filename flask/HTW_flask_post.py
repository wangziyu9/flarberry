/ encoding:utf-8
import time
from flask import Flask,render_template,request,jsonify
import ralay_switch
import config_json_by_time
import config_json
<<<<<<< HEAD
/ from gpiozero import LED
=======
from gpiozero import LED
>>>>>>> 9074a210041957080cca204d293ccf4c7ec9131c

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
    return render_template("HTW_charts.html")

<<<<<<< HEAD
=======
@app.route('/watering')
def watering():
    return render_template("watering_switch.html")
>>>>>>> 9074a210041957080cca204d293ccf4c7ec9131c

@app.route('/watering_off')
def watering_off():
    ralay_switch.stop()
    return render_template("watering_switch.html")
<<<<<<< HEAD
=======

@app.route('/watering_on')
def watering_on():
    ralay_switch.watering(50)
    return render_template("watering_switch.html")

>>>>>>> 9074a210041957080cca204d293ccf4c7ec9131c
@app.route('/watering_once')
def watering_once():
    ralay_switch.watering()
    return render_template("watering_switch.html")

<<<<<<< HEAD
@app.route('/watering_on_10')
def watering_on_10():
    ralay_switch.watering(10)
    return render_template("watering_switch.html")
@app.route('/watering_on_30')
def watering_on_30():
    ralay_switch.watering(30)
    return render_template("watering_switch.html")
@app.route('/watering_on_60')
def watering_on_60():
    ralay_switch.watering(60)
    return render_template("watering_switch.html")


=======
>>>>>>> 9074a210041957080cca204d293ccf4c7ec9131c
@app.route('/data', methods=['GET', 'POST'])
def rtn_data():
    d = config_json.get_data()
    # d = config_json_by_time.get_data_by_time_list()
    return jsonify(d)

@app.route('/data/day', methods=['GET', 'POST'])
def rtn_data_by_day():
<<<<<<< HEAD
    # / d = config_json.get_data()
    d = config_json_by_time.get_data_by_time_list(DAY)
    return jsonify(d)
@app.route('/data/hour', methods=['GET', 'POST'])
def rtn_data_by_hour():
    # / d = config_json.get_data()
    d = config_json_by_time.get_data_by_time_list(HOUR)
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True) / debug = True)
=======
    # d = config_json.get_data()
    d = config_json_by_time.get_data_by_time_list(DAY)
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True) # debug = True)
>>>>>>> 9074a210041957080cca204d293ccf4c7ec9131c
