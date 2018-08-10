#!/bin/sh
import os
import sys
try:
    os.environ["LINE_TOKEN"]
except KeyError: 
    print("Environment variables \"LINE_TOKEN\" does not setup, please set it up first.")
    sys.exit(1)

from linebot import LineBotApi
from linebot.models import TextSendMessage
line_bot_api = LineBotApi(os.environ["LINE_TOKEN"])

def push_message(user_id:str, message:str):
    #push message to one user
    line_bot_api.push_message(user_id, TextSendMessage(text=message))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python {} type user_id message ".format(__file__))
        sys.exit(1)

    if sys.argv[1] == "single":
        push_message(sys.argv[2], sys.argv[3])