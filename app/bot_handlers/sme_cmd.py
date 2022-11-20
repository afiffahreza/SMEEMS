from linebot.models import FlexSendMessage
from app.config.line import line_bot_api
from app.services.users import get_user
from app.services.subscriptions import get_subscriptions, create_subscription, get_subscription, delete_subscription
from app.services.plans import get_plan, get_plans
from app.services.smes import get_sme, get_smes
from app.bot_handlers.msg_templates import createFlexBubbleSMEs, createFlexBubbleSMEInfo, createFlexBubbleSMEPlans, createFlexBubbleError, createFlexBubbleSuccess
import uuid

print('Loading sme commands...')

def command_smes_list(event):
    smes = get_smes()
    if len(smes) > 0:
        flexMessage = createFlexBubbleSMEs(smes)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='Available SMEs', contents=flexMessage)
        )
    else:
        error_msg = 'No SME found'
        flexMessage = createFlexBubbleError(error_msg)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=error_msg, contents=flexMessage)
        )


def command_sme_info(event, sme_id):
    sme = get_sme(sme_id)
    if sme is not None:
        flexMessage = createFlexBubbleSMEInfo(sme)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='SME Info', contents=flexMessage)
        )
    else:
        error_msg = 'SME not found'
        flexMessage = createFlexBubbleError(error_msg)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=error_msg, contents=flexMessage)
        )


def command_plans_list(event, sme_id):
    sme = get_sme(sme_id)
    if sme is not None:
        plans = get_plans(sme['id'])
        if len(plans) > 0:
            flexMessage = createFlexBubbleSMEPlans(sme, plans)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text='Available Plans', contents=flexMessage)
            )
        else:
            error_msg = 'No plan found'
            flexMessage = createFlexBubbleError(error_msg)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text=error_msg, contents=flexMessage)
            )
    else:
        error_msg = 'SME not found'
        flexMessage = createFlexBubbleError(error_msg)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=error_msg, contents=flexMessage)
        )


def command_subscribe(event, plan_id):
    user = get_user(event.source.user_id)
    if user is not None:
        plan = get_plan(plan_id)
        if plan is not None:

            # check if the user already have the same plan
            subscriptions = get_subscriptions(user['id'])
            for subscription in subscriptions:
                if subscription['plan_id'] == plan['id']:
                    error_msg='You already have the plan'
                    flexMessage = createFlexBubbleError(error_msg)
                    line_bot_api.reply_message(
                        event.reply_token,
                        FlexSendMessage(alt_text=error_msg, contents=flexMessage)
                    )
                    return

            sme = get_sme(plan['sme_id'])
            text_reply='You have subscribed to ' + sme['name'] + ' ' + plan['name']
            id = str(uuid.uuid4())
            subscription_data = {
                'id': id,
                'user_id': user['id'],
                'plan_id': plan['id'],
                'status': 'inactive',
                'start_date': '-',
                'end_date': '-'
            }
            create_subscription(subscription_data)

            flexMessage = createFlexBubbleSuccess(text_reply)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text=text_reply, contents=flexMessage)
            )

        else:
            text_reply='Plan not found'
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

def command_unsubscribe(event, subscription_id):
    # check if subscription exist
    subscription = get_subscription(subscription_id)
    if subscription is not None:
        # check if the subscription is owned by the user
        if subscription['user_id'] == event.source.user_id:
            # delete the subscription
            delete_subscription(subscription_id)
            text_reply='You have unsubscribed from the plan'
            flexMessage = createFlexBubbleSuccess(text_reply)
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text=text_reply, contents=flexMessage)
            )
    else:
        text_reply='Subscription not found'
        flexMessage = createFlexBubbleError(text_reply)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=text_reply, contents=flexMessage)
        )
