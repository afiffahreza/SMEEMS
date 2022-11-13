from linebot.models import TextSendMessage
from app.config.line import line_bot_api

print('Loading ping command...')

def command_ping(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Pong!'))