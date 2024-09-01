from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)

from linebot.exceptions import (InvalidSignatureError)

from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

from AI import generate_response

import re

import card

app = Flask(__name__)

token = 'cxPJsNliFE3msdzd3KzlSiCR4ZaM0LGYUlF4OjzTe9OlaAJc8MpWfcrRl7/VYMl66RANQGMzYKgG3RinYw0b7+/VK/q8C2fM2+5o12w2mIabMvgV0y33UiycweijienFcg+L4CAP59q1z8LjSQfZPAdB04t89/1O/w1cDnyilFU='
secret = '67cf34073a27de5d3e53d18cd66aa372'
line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)


@app.route('/callback', methods=['POST'])
def callback():
  signature = request.headers['X-Line-Signature']
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    print(
        "Invalid signature. Please check your channel access token/channel secret."
    )
    abort(400)

  return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  message = event.message.text

  if len(message.split("\n")) > 1:
    question = message.split("\n")[0]
    method = message.split("\n")[1]

  else:
    method = message
    question = '抽牌結果：'

  if re.match("說明", method):
    reply_message = card.guide()

  elif re.match("1", method) or re.match("抽牌", method):
    reply_message = card.draw_one_cards(question)

  elif re.match("2", method) or re.match("時間之流", method) or method in "時間之流":
    reply_message = card.draw_timeflow_cards(question)

  elif re.match("3", method) or re.match("抽聖三角", method) or method in "聖三角":
    reply_message = card.draw_triangle_cards(question)

  elif re.match("4", method) or re.match("抽六芒星", method) or method in "六芒星":
    reply_message = card.draw_sixstar_cards(question)

  elif re.match("5", method) or re.match("抽無牌陣", method) or method in "無牌陣":
    reply_message = card.draw_three_cards(question)

  elif re.match("6", method) or re.match("抽關係牌", method) or method in "關係牌":
    reply_message = card.draw_relation_cards(question)
    
  else:
    #reply_message = "我看不懂你說啥_(┐「ε:)_"
    reply_message = generate_response(message)

  line_bot_api.reply_message(event.reply_token,
                             TextSendMessage(text=reply_message))


app.run(host='0.0.0.0', port=8080)
