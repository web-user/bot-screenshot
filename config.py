import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app_m.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_TEL = '1336773122:AAGQILgpbaJ-TJdQTpLf-_VIDzWhtUI_aAM'


