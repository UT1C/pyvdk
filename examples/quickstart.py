from flask import Flask, request
from pyvdk import Bot, Config


app = Flask(__name__)
config = Config(
    token="",
    v=5.103,
    group_id=,
    secret="",
    confcode=""
)
bot = Bot(config)


@app.route('/', methods=['POST'])
def bot_route():
    return bot.request_handle(request.get_json())


@bot.on.message_new(text='test')
def test_func(msg: object):
    print('brrrr')
    msg('brrrrrrr')