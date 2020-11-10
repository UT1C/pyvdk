from flask import Flask, request
from pyvdk import Bot, Config, types
import os


app = Flask(__name__)
config = Config(
    token=os.environ["BOT_TOKEN"],
    secret=os.environ["BOT_SECRET"],
    confcode=os.environ["BOT_CONFIRMATION_CODE"],
    group_id=0
)
bot = Bot(config)


@app.route('/', methods=['POST'])
def bot_route():
    return bot.request_handle(request.get_json())


@bot.on.message_new(text='/test')
def test_func(msg: types.Message):
    msg('brrrrrrr')


if __name__ == "__main__":
    # localhost
    app.run("127.0.0.1", port=5099)