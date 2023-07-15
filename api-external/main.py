import requests
from flask import Flask,request,jsonify
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



endpoint_day = os.getenv('ENDPOINT_DAY')
endpoint_month = os.getenv('ENDPOINT_MONTH')
secret = os.getenv('API_SECRET')

@app.route('/v1/api/printday', methods=['POST'])
def printDay():
    y = requests.post(endpoint_day, headers={secret})
    resp = jsonify(success=True)
    return resp

@app.route('/v1/api/printmonth', methods=['POST'])
def printMonth():
    y = requests.post(endpoint_month, headers={'apikey': secret})
    resp = jsonify(success=True)
    return resp

@app.route("/healthz")
def default():
    return "",200

@app.route("/")
def default():
    return "",200

if __name__ == '__main__':
  app.run(port=int(os.getenv('PORT', 3000)),use_reloader=False)