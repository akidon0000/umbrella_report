from flask import Flask, request, abort
import os
import datetime
from os.path import join, dirname
from dotenv import load_dotenv

# import logging
# from multiprocessing import Pool
# from scheduler.job import JobController
import schedule
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

  # 10分ごと
  # schedule.every(10).minutes.do(report)

  # 2時間ごと
  # schedule.every(2).hours.do(report)

  # 毎日0時1分
  schedule.every().day.at("00:01").do(report)

  # 毎週月曜日
  # schedule.every().monday.do(report)

  while True:
      schedule.run_pending()
      time.sleep(1)



def report():
  dt_now = datetime.datetime.now()

  log_file_name = str(datetime.date(dt_now.year, dt_now.month, dt_now.day)) + ".log"

  path = "./logFiles/" + log_file_name

  if os.path.exists(path):
    line_bot_api.broadcast(TextSendMessage(text="サーバーにERRORが発生しています"))

    f = open(path, 'r')
    data = f.read()
    f.close()
    line_bot_api.broadcast(TextSendMessage(text="==ERROR内容==\n" + data))

  else:
    line_bot_api.broadcast(TextSendMessage(text="サーバーは正常に稼働中"))


if __name__ == "__main__":
    main()
