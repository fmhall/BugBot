import requests
import time
request_params = {'token': 'xxxx'}
while True:
    response_messages = requests.get('https://api.groupme.com/v3/groups/your_groupID_here/messages', params = request_params).json()['response']['messages']
    message = response_messages[0]
    print(message['text'],message['name'])
    if ('I️'   in message['text']):
        to_send = 'Please fix your phone, ' + message['name'] + "! Go to settings > general > keyboard > text replacement > + and add the shortcut I > I and it will fix it. Or, update your phone! It really isn't that hard."
        post_params = { 'bot_id' : 'yyyyy', 'text': to_send }
        requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
    time.sleep(5)
