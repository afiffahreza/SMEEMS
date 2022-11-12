from linebot import LineBotApi
from linebot.models import TextSendMessage
from app.config import CHANNEL_ACCESS_TOKEN

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def command_hello(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hello World!'))