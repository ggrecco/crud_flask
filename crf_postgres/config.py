import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-shall-not-pass'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgre$fhgv@192.168.1.6:5432/bd_proris'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'pt']
