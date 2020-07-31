import os
import telebot
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from telebot import types
from datetime import datetime
from flask import render_template, abort, flash, redirect, url_for, session, request, g, \
    jsonify, current_app
import datetime, pytz, requests
from app import create_app
from app.main import bp

from PIL import Image
from io import BytesIO

from config import Config
import random
import time

app = create_app()

secret = Config.TOKEN_TEL
bot = telebot.TeleBot(Config.TOKEN_TEL, threaded=False)

# setWebhook url
# https://api.telegram.org/bot1079440246:AAGPq-ujFyK6pRIJTMYt0btfpztS0cwjmkg/setWebhook?url=https://appm-pk.herokuapp.com/1079440246:AAGPq-ujFyK6pRIJTMYt0btfpztS0cwjmkg
URL = 'https://api.telegram.org/bot{}/'.format(Config.TOKEN_TEL)


def screenshot_bot(url):

    outputdir = os.path.abspath(os.getcwd())

    # options = webdriver.ChromeOptions()
    chrome_options = Options()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN") - heroku.
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # executable_path = os.environ.get("CHROMEDRIVER_PATH") - heroku.
    driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
    driver.get(url)
    time.sleep(2)

        #the element with longest height on page
    ele=driver.find_element("xpath", '//body')
    total_height = ele.size["height"]+200

    driver.set_window_size(1920, total_height)      #the trick
    time.sleep(2)

    driver.save_screenshot("{}/img/screenshot-2.png".format(outputdir))
    driver.close()

    image = Image.open("{}/img/screenshot-2.png".format(outputdir))
    width, height = image.size

    if height > 3000:
        image = image.resize((1500,3500))
        fpath = BytesIO()
        image.save("{}/img/screenshot-2.png".format(outputdir), 'PNG', dpi=[800, 600], quality=40)
        fpath.seek(0)


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


@bp.route('/{}'.format(secret), methods=['GET', 'POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


#         START
@bot.message_handler(commands=['start', 'help'])
def startCommand(message):
    # keyboard
    bot.send_message(message.chat.id, 'Hi *' + message.chat.first_name + '*!', parse_mode='Markdown')

"""
message handler.
"""
@bot.message_handler(content_types=['text'])
def lalala(message):
    outputdir = os.path.abspath(os.getcwd())
    if message.chat.type == 'private':
        logging.info('This is an info message')
        logging.info(message.text)

        try:
            url_val = response= requests.get(message.text)
            status = response.status_code
            screenshot_bot(message.text)
            msgid = message.message_id
            logging.info('This is an info message')

            bot.send_chat_action(message.chat.id, 'upload_photo')
            with open("{}/img/screenshot-2.png".format(outputdir), 'rb') as photo:
                bot.send_photo(message.chat.id, photo, reply_to_message_id=msgid)


        except:
            bot.send_message(message.chat.id, 'Url not valid! 😢')

