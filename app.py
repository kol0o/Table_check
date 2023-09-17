from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname

app = Flask(__name__)


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    print(request.json)
    return os.environ.get(key)


def send_message(chat_id, text):
    method = 'sendMessage'
    token = get_from_env('TELEGRAM_BOT_TOKEN')
    url = f'https://api.telegram.org/bot{token}/{method}'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)


@app.route('/', methods=['POST'])
def process():  # put application's code here
    chat_id = request.json['message']['chat']['id']
    send_message(chat_id=chat_id, text='Hi man')
    return {'ok': True}


if __name__ == '__main__':
    app.run()
