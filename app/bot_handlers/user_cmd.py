from linebot.models import TextSendMessage
from app.config.line import line_bot_api
from app.services.users import create_user

print('Loading user commands...')

def command_help(event):
    text_reply='Available commands:\n'
    text_reply += 'smeems ping\n'
    text_reply += 'smeems help\n'
    text_reply += 'smeems register <email>\n'
    text_reply += 'smeems smes\n'
    text_reply += 'smeems sme <sme_id>\n'
    text_reply += 'smeems plans <sme_id>\n'
    text_reply += 'smeems subscriptions\n'
    text_reply += 'smeems subscribe <plan_id>\n'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))

def command_register(event, email):
    profile = line_bot_api.get_profile(event.source.user_id)
    user_data = {
        'id': event.source.user_id,
        'name': profile.display_name,
        'email': email,
        'line_uid': event.source.user_id
    }
    create_user(user_data)
    text_reply='Hi ' + profile.display_name + ', you are now registered with email ' + email
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))
