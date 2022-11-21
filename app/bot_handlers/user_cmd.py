from linebot.models import TextSendMessage, FlexSendMessage
from app.config.line import line_bot_api
from app.services.users import create_user, get_user
from app.services.subscriptions import get_subscriptions, get_subscription
from app.services.steppay import create_steppay_user, create_steppay_invoice
from app.services.plans import get_plan
from app.bot_handlers.msg_templates import createFlexBubbleError, createFlexBubbleSuccess, createFlexBubbleSubscriptionList


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