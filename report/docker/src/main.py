from flask import Flask, request, abort
import os
import datetime
from os.path import join, dirname
from dotenv import load_dotenv

# import logging
# from multiprocessing import Pool
# from scheduler.job import JobController
# import schedule
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
  # 10分ごと
  # schedule.every(10).minutes.do(report)

  # 2時間ごと
  # schedule.every(2).hours.do(report)

  # 毎日0時1分
  # schedule.every().day.at("00:01").do(report)

  # 毎週月曜日
  # schedule.every().monday.do(report)

  # while True:
  #     schedule.run_pending()
  #     time.sleep(30)
  report()



def report():

  dt_now = datetime.datetime.now()


  log_file_name = str(datetime.date(dt_now.year, dt_now.month, dt_now.day-1)) + ".log"
  print(dt_now)
  print(log_file_name)
  line_bot_api.broadcast(TextSendMessage(text=str(dt_now)))
  line_bot_api.broadcast(TextSendMessage(text=log_file_name))

  errorPath = "/python/src/logFiles/ErrorLogFiles/" + log_file_name
  successPath = "/python/src/logFiles/SuccessLogFiles/" + log_file_name



  # Success
  if os.path.exists(successPath):
    f = open(successPath, 'r')
    data = f.read()
    f.close()

    successCount = data.count("[Success]")
    line_bot_api.broadcast(TextSendMessage(text="==本日の稼働状況==\n" + "通信回数：" + str(successCount)))

  else:
    line_bot_api.broadcast(TextSendMessage(text="==本日の稼働状況==\n" + "通信回数：" + "0"))


  # ErrorPath
  if os.path.exists(errorPath):
    line_bot_api.broadcast(TextSendMessage(text="サーバーにERRORが発生しています"))

    f = open(path, 'r')
    data = f.read()
    f.close()
    line_bot_api.broadcast(TextSendMessage(text="==ERROR内容==\n" + data))

  else:
    line_bot_api.broadcast(TextSendMessage(text="サーバーは正常に稼働中"))


if __name__ == "__main__":
    main()
