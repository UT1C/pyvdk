from flask import Flask, request
from pyvdk import Bot, Config


app = Flask(__name__)
config = Config().from_yaml('config.yaml')
bot = Bot(config)


@app.route('/', methods=['POST'])
def bot_route():
    return bot.request_handle(request.get_json())


@bot.on.message_new(text='test')
def test_func(msg: object):
    print('brrrr')
    msg('brrrrrrr')