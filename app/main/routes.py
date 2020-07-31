import requests
from flask import render_template, redirect, url_for, request, current_app
from app import create_app

from app.main import bp

from config import Config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging

from selenium import webdriver
import os
import time

app = create_app()


@bp.route('/', methods=['POST', 'GET'])
def index():
    data_test = {"name":"vasa", "age":28}
    # print(app.config['CELERY_BROKER_URL'])
    return render_template('index.html', data=data_test)


