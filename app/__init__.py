from flask import Flask, request, abort
from flask_cors import CORS

from app.bot_handlers import handler
from linebot.exceptions import (
    InvalidSignatureError
)

app = Flask(__name__)

# handle cors with flask-cors
CORS(app)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# hello world in /
@app.route("/")
def hello():
    return "Hello World!"
