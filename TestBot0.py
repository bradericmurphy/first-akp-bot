import requests
import os

request_params = {'token': 'os.getenv('GROUPME_BOT_ID')'}
while true:
    response_messages = requests.get('https://api.groupme.com/v3/groups/39940851/messages', params = request_params).json()['response']['messages']

    for message in response_messages['messages']:
        print message['text']