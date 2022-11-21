from linebot.models import (
    MessageEvent, TextMessage,
)
from app.bot_handlers.ping import command_ping
from app.bot_handlers.user_cmd import command_help, command_register, command_subscription_list, command_pay
from app.bot_handlers.sme_cmd import command_smes_list, command_sme_info, command_plans_list, command_subscribe, command_unsubscribe
from app.bot_handlers.promo_cmd import command_promo
from app.config.line import handler

print('Loading handlers...')

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text.startswith('smeems '):
        command = text.split(' ')[1]
        print("Command: " + command)
        if command == 'ping':
            command_ping(event)
        elif command == 'help':
            command_help(event)
        elif command == 'register':
            email = text.split(' ')[2]
            command_register(event, email)
        elif command == 'smes':
            command_smes_list(event)
        elif command == 'sme':
            sme_id = text.split(' ')[2]
            command_sme_info(event, sme_id)
        elif command == 'plans':
            sme_id = text.split(' ')[2]
            command_plans_list(event, sme_id)
        elif command == 'subscriptions':
            command_subscription_list(event)
        elif command == 'subscribe':
            plan_id = text.split(' ')[2]
            command_subscribe(event, plan_id)
        elif command == 'unsubscribe':
            subscription_id = text.split(' ')[2]
            command_unsubscribe(event, subscription_id)
        elif command == 'promo':
            sme_id = text.split(' ')[2]
            command_promo(event, sme_id)
        elif command == 'pay':
            subscription_id = text.split(' ')[2]
            command_pay(event, subscription_id)