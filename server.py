import requests
import json

api_url = "http://navprod1.corp.unicity.net:8047/NAV2018_TEST/WS/Interface/Codeunit/Testingtestserver"
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
        jsonStr = {"type": "message",  "message": {"type": "text", "id": "17303396215923",   "text": "/code50013"}, "webhookEventId": "01GMCJMSVG10SCZ9V1SPGZSPQH", "deliveryContext": {"isRedelivery": False}, "timestamp": 1671164487180, "source": { "type": "user", "userId": "Ua36030c425e62bd7ea0182d13ddabfdb" }, "replyToken": "77a6cdd9f71840e2ae45cb0883b75515", "mode": "active"}
        jsonStr2 = jsonStr['message']['text']
        print(jsonStr2)
        print("response NAV: ")
        #response = requests.post(httpurl, json=todo, auth=HTTPBasicAuth('trinhfpt', 'Unicity@2020'))
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