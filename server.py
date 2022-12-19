import requests
import json

api_url = "http://navprCodeunit/Testingtestserver"
from flask import Flask, request, abort
app = Flask(__name__)
from requests.auth import HTTPBasicAuth
httpurl = 'SoapUrl'
# Making a get request
todo = {"userId": 1, "title": "Buy milk", "completed": False}
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        jsonStr = request.json
        jsonStr = {"type": "message",  "message": {"type": "text", "id": "173033",   "text": "/code50013"}, "webhookEventId": "01GM1SPGZSPQH", "deliveryContext": {"isRedelivery": False}, "timestamp": 16717180, "source": { "type": "user", "userId": "Ua36030c4d13ddabfdb" }, "replyToken": "77a6cdd9f71840e2ae45cb0883b75515", "mode": "active"}
        jsonStr2 = jsonStr['message']['text']
        print(jsonStr2)
        print("response NAV: ")
        #response = requests.post(httpurl, json=todo, auth=HTTPBasicAuth('trinhfp8t', 'Un20'))
        return 'success reciver', 200
    else:
        print('kiem tra fail')
        return '400'
@app.route('/webhook', methods=['GET'])
def webhook1():
    if request.method == 'GET':
        print('you send get')
        return 'success', 200
    else:
        print('kiem tra GET')
        return '400'
if __name__ == '__main__':
    app.run()
