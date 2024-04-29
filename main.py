from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
)

import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time






#Token取得

YOUR_CHANNEL_ACCESS_TOKEN = "Your Access Token"
YOUR_CHANNEL_SECRET = "Your channel secret"

app = Flask(__name__)
app.debug = False

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)




@app.route("/")
def home():
    return "OK"

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
    
    if event.message.text == "test":
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Server working')
                )  
    #input = image number serchkeyword
    elif event.message.text.startswith("image"):
        serch = event.message.text.replace("image","").strip()
        numAndserch =  serch.split(" ")

        print(numAndserch)

        numOfImage = int(numAndserch[0])
        if numOfImage>=5:
            numOfImage =5

        print(numOfImage)#test
        serchWord = numAndserch[1]
        from getImage import gettingImage as GI
        imgs = GI(serchWord,numOfImage)
        sendMessages =[]
        for img in imgs:
            image_message = ImageSendMessage(
                original_content_url= img,
                preview_image_url= img,
            )
            sendMessages.append(image_message)

        print(f"len :{len(sendMessages)}")
        line_bot_api.reply_message(event.reply_token, sendMessages)

    else: 
        serch = event.message.text
        from getImage import gettingImage as GI
        imgs = GI(serch,1)
        sendMessages =[]
        for img in imgs:
            image_message = ImageSendMessage(
                original_content_url= img,
                preview_image_url= img,
            )
            sendMessages.append(image_message)
        line_bot_api.reply_message(event.reply_token, sendMessages)

if __name__ == "__main__":
    port = int(os.getenv("PORT",5001))
    app.run(host="0.0.0.0", port=port)
