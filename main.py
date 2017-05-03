import client
import json

configfile = open('config.json')
config = json.loads(configfile.read())
configfile.close()

while True:
    new_messages = client.check()
    for message in new_messages:
        if message['content'].lower().startswith(config['prefix'] + 'python'):
            client.send(message['channel'], 'This is a python plugin!')
