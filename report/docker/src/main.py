from flask import Flask, request, abort
import os
import datetime
from os.path import join, dirname
from dotenv import load_dotenv

import time

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

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def main():
  # line_bot_api.broadcast(TextSendMessage(text="メンテナンス"))
  report()


def report():

  dt_now = datetime.datetime.now()

  time = str(datetime.date(dt_now.year, dt_now.month, dt_now.day-1))
  log_file_name = time + ".log"
  print(dt_now)
  print(log_file_name)
  textMessage = ""
  textMessage += "===" + time + "===\n"

  errorPath = "/python/src/logFiles/ErrorLogFiles/" + log_file_name
  successPath = "/python/src/logFiles/SuccessLogFiles/" + log_file_name



  # Success
  if os.path.exists(successPath):
    f = open(successPath, 'r')
    data = f.read()
    f.close()

    successCount = data.count("[Success]")
    textMessage += "通信回数：" + str(successCount) + "\n"

  else:
    textMessage += "通信回数：0\n"


  # ErrorPath
  if os.path.exists(errorPath):
    textMessage += "サーバー:ERROR\n"
    f = open(path, 'r')
    data = f.read()
    f.close()
    textMessage += "==ERROR内容==\n" + data

  else:
    textMessage += "サーバー:正常"

  line_bot_api.broadcast(TextSendMessage(text=textMessage))

if __name__ == "__main__":
    main()
