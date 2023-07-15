from flask import Flask,request,jsonify
from datetime import date
import calendar
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

secret = os.getenv('API_SECRET')

@app.route('/v1/api/printmonth', methods=['POST'])
def printMonth():
    if request.headers['apikey'] == secret:
        month = calendar.month_name[date.today().month]
        logger.info('month: %s',month)
    resp = jsonify(success=True)
    return resp

@app.route("/healthz")
def default():
    return "",200

@app.route("/")
def default():
    return "",200

if __name__ == '__main__':
  app.run(port=int(os.getenv('PORT', 4000)),use_reloader=False)
