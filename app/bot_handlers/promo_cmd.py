from linebot.models import TextSendMessage
from app.config.line import line_bot_api
from app.services.smes import get_sme
import requests

print('Loading promo commands...')

# Request post to langcode api
# https://hack-3.langcode.io/api/Hackathon/SendMessageToBot
# {
#   "botId": "ed40f64c-31fa-4a02-b45d-0816a34a1e14",
#   "userId": "smeems_bot",
#   "text": "question"
# }
def langcode_mw(sme_id):
    # get sme name
    sme = get_sme(sme_id)
    sme_name = sme['name']
    # generate question using sme name
    question = 'What is the promo for ' + sme_name + '?'
    # request to langcode
    req_msg = {
        "botId": "ed40f64c-31fa-4a02-b45d-0816a34a1e14",
        "userId": "smeems_bot",
        "text": question
    }
    req = requests.post('https://hack-3.langcode.io/api/Hackathon/SendMessageToBot', json=req_msg)
    return req.json()

def command_promo(event, sme_id):
    text_reply='Promo info:\n'
    text_reply += 'Promo 1\n'
    text_reply += 'Promo 2\n'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))