import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-shall-not-pass'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@192.168.0.105:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'pt']
