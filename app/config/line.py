from linebot import LineBotApi, WebhookHandler
from . import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET

print('Loading Line Bot API...')
handler = WebhookHandler(CHANNEL_SECRET)
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)