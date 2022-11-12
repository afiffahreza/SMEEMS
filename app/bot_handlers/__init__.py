from linebot import WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage,
)
from app.bot_handlers.hello import command_hello
from app.config import CHANNEL_SECRET

handler = WebhookHandler(CHANNEL_SECRET)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text.startswith('smeems '):
        command = text.split(' ')[1]
        print("Command: " + command)
        if command == 'hello':
            command_hello(event)