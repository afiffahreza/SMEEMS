from linebot.models import TextSendMessage, FlexSendMessage
from app.config.line import line_bot_api
from app.services.users import get_user
from app.services.subscriptions import get_subscriptions, create_subscription
from app.services.plans import get_plan, get_plans
from app.services.smes import get_sme, get_smes
import uuid
import copy

print('Loading sme commands...')

contentTemplate = {
    "type": "button",
    "action": {
        "type": "message",
        "label": "Placeholder",
        "text": "uuid"
    },
    "style": "primary",
    "color": "#FF735C",
    "margin": "md"
}

bubbleJSON = {
    "type": "bubble",
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "Pick a SME!",
                "margin": "lg",
                "size": "xxl",
                "weight": "bold"
            }
        ],
        "spacing": "xs",
        "margin": "md",
        "alignItems": "center"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "action": {
            "type": "message",
            "label": "action",
            "text": "hello"
        }
    }
}


def createFlexBubbleSMEs(smes):
    temp = []
    for i in smes:
        tempTemplate = copy.deepcopy(contentTemplate)

        tempTemplate["action"]["label"] = i["name"]
        tempTemplate["action"]["text"] = i["id"]

        temp.append(tempTemplate)

    bubbleJSON["body"]["contents"] = temp
    return bubbleJSON


def command_smes_list(event):
    smes = get_smes()
    if len(smes) > 0:
        flexMessage = createFlexBubbleSMEs(smes)
        print(flexMessage)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='Available SMEs', contents=flexMessage)
            # TextSendMessage(text=flexMessage)
        )
    else:
        text_reply = 'No SME found'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text_reply)
        )


def command_sme_info(event, sme_id):
    sme = get_sme(sme_id)
    if sme is not None:
        text_reply = 'SME info:\n'
        text_reply += 'Name: ' + sme['name'] + '\n'
        text_reply += 'Email: ' + sme['email'] + '\n'
    else:
        text_reply = 'SME not found'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))


def command_plans_list(event, sme_id):
    sme = get_sme(sme_id)
    if sme is not None:
        plans = get_plans(sme['id'])
        if len(plans) > 0:
            text_reply = 'Available plans for ' + sme['name'] + ':\n'
            for plan in plans:
                text_reply += plan['id'] + ' ' + plan['name'] + '\n'
        else:
            text_reply = 'No plan found for ' + sme['name']
    else:
        text_reply = 'SME not found'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))


def command_subscription_list(event):
    user = get_user(event.source.user_id)
    if user is not None:
        subscriptions = get_subscriptions(user['id'])
        if len(subscriptions) > 0:
            text_reply='Your subscriptions:\n'
            for subscription in subscriptions:
                plan = get_plan(subscription['plan_id'])
                sme = get_sme(plan['sme_id'])
                text_reply += sme['name'] + ' ' + plan['name'] + '\n'
        else:
            text_reply='You have no subscription'
    else:
        text_reply='You are not registered'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))


def command_subscribe(event, plan_id):
    user = get_user(event.source.user_id)
    if user is not None:
        plan = get_plan(plan_id)
        if plan is not None:
            sme = get_sme(plan['sme_id'])
            text_reply='You have subscribed to ' + sme['name'] + ' ' + plan['name']
            id = str(uuid.uuid4())
            subscription_data = {
                'id': id,
                'user_id': user['id'],
                'plan_id': plan['id'],
                'status': 'active',
                'start_date': '2022-11-16',
                'end_date': '2022-12-16'
            }
            create_subscription(subscription_data)
        else:
            text_reply='Plan not found'
    else:
        text_reply='You are not registered'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text_reply))
