from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('w0MHmdKL5rngRbvcIg+4FLmB5hbMWuh8TGhiCDGNVEW1OVk7K5zslbkIjJeRNlcy2hS271orpznnXOPetgmP30f1dCVx8uN+YSCLbNyCCtmVaMNfvklhgAuqUAUSwdTG8U+OBc2vIY7V0WZE+7xuQwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b20b1e2ab35edf26d68cfcec1e3a93e0')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    msg = event.message.text + " 愛你喔!"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))


if __name__ == "__main__":
    app.run()


