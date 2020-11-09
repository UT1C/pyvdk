from flask import Flask, request
from pyvdk import Bot, Config


app = Flask(__name__)
bot = Bot(
    Config(
        token="token",
        v=5.103,
        group_id=0,
        secret="secret",
        confcode="confcode"
    )
)


@app.route('/', methods=['POST'])
def bot_route():
    return bot.request_handle(request.get_json())


@bot.on.message_new(text='/test')
def test_func(msg: object):
    print('brrrr')
    msg('brrrrrrr', msg.peer_id)