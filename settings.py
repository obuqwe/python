import requests
from time import sleep
from bot_settings import token_bot

token = token_bot
api_url = "https://api.telegram.org/bot{}".format(token)
listening = True

def get_updates(limit = 10, offset = 0):
    method_url = "{}/getUpdates".format(api_url)
    params = {"offset" : offset, "limit" : limit}
    response = requests.get(method_url, params = params)
    result = response.json()
    #print(result)
    return result
def send_message(chat_id, text):
    method_url = "{}/sendMessage".format(api_url)
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(method_url, params = params)
    result = response.json()
    #print(result)

offset = 0
while listening:
    updates = get_updates(offset = offset)
    print(updates)
    result = updates['result']
    if result:
        update_id = result[0]['update_id']
        offset = update_id + 1
        chat_id = result[0]['message']['chat']['id']
        send_message(chat_id, 'Hello!')
    sleep(1)