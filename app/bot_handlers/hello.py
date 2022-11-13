from linebot.models import TextSendMessage
from app.config.line import line_bot_api

print('Loading hello command...')

def command_hello(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hello, World!'))