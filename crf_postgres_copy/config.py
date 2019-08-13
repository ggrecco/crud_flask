import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-shall-not-pass'
    LANGUAGES = ['en', 'pt']
