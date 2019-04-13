import time
from flask import Flask,render_template,request,jsonify
import ralay_switch
import config_json_by_time
import config_json

app = Flask(__name__)
ralay_gpio = 24
ralay = 0

MINUTE = 60
HOUR = 60 * MINUTE
HOUR2 = HOUR * 2
DAY = 24 * HOUR
WEEK = 7 * DAY 
MONTH = 30 * DAY

print(config_json_by_time.get_data_by_time_list(HOUR))
