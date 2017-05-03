import requests
import json

def send(channelid, message):
    return requests.post('http://localhost:3000/send', json={'channelid': channelid, 'message': message})
def check():
    return json.loads(requests.get('http://localhost:3000/check').text)
