
import json
from requests.auth import HTTPBasicAuth
import requests

httpurl = 'http://127.0.0.1:5000/webhook';
# Making a get request
todo = {"userId": 1, "title": "Buy milk", "completed": False}

#response = requests.get(httpurl, auth=HTTPBasicAuth('trinhfpt', 'Unicity@2020'))
response = requests.post(httpurl, json=todo, auth=HTTPBasicAuth('trinhfpt', 'Unicity@2020'))
#response = requests.get(httpurl)
print(response.headers,'- - ', response.text)