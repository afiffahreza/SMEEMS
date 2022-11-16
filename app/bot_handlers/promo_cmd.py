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
# Example response:
# [
#   {
#     "id": "2979d12f-b7d0-421d-ab49-c096ba7710c4",
#     "sessionId": "hack:ed40f64c-31fa-4a02-b45d-0816a34a1e14:string",
#     "senderId": "ed40f64c-31fa-4a02-b45d-0816a34a1e14",
#     "sentDate": "2022-11-16T14:00:09.8537198Z",
#     "text": "I think the answer is '646-431-0606'\nPlease refer to the document for more detail.",
#     "answer": {
#       "shortAnswer": "646-431-0606",
#       "answer": "646-431-0606",
#       "document": {
#         "id": "72da3d73-c085-446d-a6e6-08d3e8edb440",
#         "botId": "ed40f64c-31fa-4a02-b45d-0816a34a1e14",
#         "type": "pdf",
#         "title": "Restaurant Discount Flyer Template.pdf",
#         "url": "https://langcodecxp.blob.core.windows.net/files/296812b6-02fe-44d5-bd4d-78dad91a709a/Restaurant%20Discount%20Flyer%20Template.pdf"
#       },
#       "documentPage": 1
#     }
#   }
# ]
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
    res = requests.post('https://hack-3.langcode.io/api/Hackathon/SendMessageToBot', json=req_msg)
    return res.json()

def command_promo(event, sme_id):
    # get sme name
    sme = get_sme(sme_id)
    sme_name = sme['name']
    # get promo from langcode
    promo = langcode_mw(sme_id)
    # generate reply
    if promo[0]['answer'] is not None:
        text_reply = 'Promo for ' + sme_name + ':\n'
        text_reply += promo[0]['answer']['shortAnswer']
    else :
        text_reply = 'No promo for ' + sme_name
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))