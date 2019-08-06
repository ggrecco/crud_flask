import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-shall-not-pass'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@127.0.0.1:5433/crf_bootstrap'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'pt']
