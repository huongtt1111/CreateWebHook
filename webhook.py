import requests
import json
webhook_url = 'http://127.0.0.1:5000/webhook'
data = {'name': 'devops tiena6',
        'channel URL': 'test url'}
#r = requests.post(webhook_url, data=json.dumps(data), headers={'content-type': 'application/json'} )#, auth = ('', ''))
r = requests.get(webhook_url )#, auth = ('', ''))