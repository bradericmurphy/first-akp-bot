import requests
from boto.s3.connection import S3Connection

request_params = {'token': os.environ['GROUPME_BOT_ID']}
while true:
    response_messages = requests.get('https://api.groupme.com/v3/groups/39940851/messages', params = request_params).json()['response']['messages']

    for message in response_messages['messages']:
        print message['text']