from linebot.models import (
    MessageEvent, TextMessage,
)
from app.bot_handlers.hello import command_hello
from app.bot_handlers.ping import command_ping
from app.config.line import handler

print('Loading handlers...')

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text.startswith('smeems '):
        command = text.split(' ')[1]
        print("Command: " + command)
        if command == 'hello':
            command_hello(event)
        elif command == 'ping':
            command_ping(event)