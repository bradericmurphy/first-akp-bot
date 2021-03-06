import requests
import os
import time
import json
#from boto.s3.connection import S3Connection

#if (os.environ.get('CONFIG_VAR_TEST')):
#    print("config vars working")

request_params = {'token': os.environ.get('GROUP_BOT_ID')}
print(os.environ.get('GROUP_BOT_ID'))

while True:

    response = requests.get('https://api.groupme.com/v3/groups/39940851/messages', params = request_params)

    # If there are new messages, check whether any of them are making queries to the bot
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']

        # Iterate through each message, checking its text
        for message in response_messages:
            if (message['text']=='hello'):
                to_send = 'Hello!'
                post_params = { 'bot_id' : os.environ.get('GROUPME_BOT_ID'), 'text': to_send }
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
                request_params['since_id'] = message['id']
                break

    time.sleep(5)