from linebot.models import FlexSendMessage
from app.config.line import line_bot_api
from app.services.users import create_user, get_user
from app.services.subscriptions import get_subscriptions, get_subscription, update_subscription
from app.services.steppay import create_steppay_user, create_steppay_invoice
from app.services.plans import get_plan
from app.bot_handlers.msg_templates import createFlexBubbleError, createFlexBubbleSuccess, createFlexBubbleSubscriptionList
from datetime import date
from dateutil.relativedelta import relativedelta

print('Loading user commands...')

def command_help(event):
    true = True
    help = {
        "type": "bubble",
        "hero": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "image",
                "url": "https://cdn-icons-png.flaticon.com/512/1828/1828833.png",
                "size": "50px"
            },
            {
                "type": "text",
                "text": "SMEEMS HELP",
                "margin": "lg",
                "size": "20px",
                "weight": "bold",
                "wrap": true,
                "align": "center"
            },
            {
                "type": "image",
                "url": "https://cdn-icons-png.flaticon.com/512/1828/1828833.png",
                "size": "50px"
            }
            ],
            "alignItems": "center",
            "justifyContent": "center",
            "paddingAll": "10px",
            "margin": "lg",
            "spacing": "xs"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "smeems",
                    "margin": "md",
                    "weight": "bold",
                    "color": "#FF735C"
                },
                {
                    "type": "text",
                    "text": "List out all available bot commands.",
                    "margin": "md",
                    "weight": "regular",
                    "wrap": true
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "smeems register <email>",
                    "margin": "md",
                    "weight": "bold",
                    "color": "#FF735C"
                },
                {
                    "type": "text",
                    "text": "Register your account with an email.",
                    "margin": "md",
                    "weight": "regular",
                    "wrap": true
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "smeems smes",
                    "margin": "md",
                    "weight": "bold",
                    "color": "#FF735C"
                },
                {
                    "type": "text",
                    "text": "List out all available SMEs. Click the interactive button for SME Info, Discount, and Plans.",
                    "margin": "md",
                    "weight": "regular",
                    "wrap": true
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "smeems subscriptions",
                    "margin": "md",
                    "weight": "bold",
                    "color": "#FF735C"
                },
                {
                    "type": "text",
                    "text": "List out all of your subscriptions.",
                    "margin": "md",
                    "weight": "regular",
                    "wrap": true
                }
                ]
            }
            ]
        }
    }
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='Help', contents=help)
    )

def command_register(event, email):
    # check if user already registered
    user = get_user(event.source.user_id)
    if user is None:
        profile = line_bot_api.get_profile(event.source.user_id)

        # create steppay user
        steppay_user = create_steppay_user(profile.display_name, email)

        user_data = {
            'id': event.source.user_id,
            'name': profile.display_name,
            'email': email,
            'line_uid': event.source.user_id,
            'steppay_uid': steppay_user['id']
        }
        create_user(user_data)

        text_reply='Hi ' + profile.display_name + ', you are now registered with email ' + email
        flexMessage = createFlexBubbleSuccess(text_reply)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=text_reply, contents=flexMessage)
        )
    else:
        text_reply='You are already registered'
        flexMessage = createFlexBubbleError(text_reply)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=text_reply, contents=flexMessage)
        )

def command_subscription_list(event):
    user = get_user(event.source.user_id)
    if user is not None:
        subscriptions = get_subscriptions(user['id'])
        if len(subscriptions) > 0:
            flexMessage = createFlexBubbleSubscriptionList(subscriptions)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text='Your Subscriptions', contents=flexMessage)
            )
        else:
            text_reply='You have no subscription'
            flexMessage = createFlexBubbleError(text_reply)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text=text_reply, contents=flexMessage)
            )
    else:
        text_reply='You are not registered'
        flexMessage = createFlexBubbleError(text_reply)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=text_reply, contents=flexMessage)
        )

def command_pay(event, subscription_id):
    user = get_user(event.source.user_id)
    if user is not None:
        # get subscription
        subscription = get_subscription(subscription_id)
        
        # get plan
        plan = get_plan(subscription['plan_id'])

        # create steppay invoice
        steppay_invoice = create_steppay_invoice(user['steppay_uid'], plan['steppay_price_code'])

        # update subscription to active and change start date and end date
        subscription['status'] = 'active'
        subscription['start_date'] = date.today().strftime("%d-%m-%y")
        subscription['end_date'] = (date.today() + relativedelta(months=1)).strftime("%d-%m-%y")
        update_subscription(subscription_id, subscription)

        flexMessage = createFlexBubbleSuccess(steppay_invoice)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=steppay_invoice, contents=flexMessage)
        )
    else:
        text_reply='You are not registered'
        flexMessage = createFlexBubbleError(text_reply)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=text_reply, contents=flexMessage)
        )