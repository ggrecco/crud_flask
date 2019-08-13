from app import db, login, cursor
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
import psycopg2


class Banco():
    def listar():
        cursor.execute("select * from esse.tb_esse")
        usuarios = cursor.fetchall()
        print(usuarios)
        # cursor.close()
        return 'lista'


# verifica se o loguin existe na tabela

    def login(nome, senha):
        # cursor.execute("select * from esse.tb_esse")
        # usuarios = cursor.fetchall()
        # print(usuarios)
        try:
            cursor.execute(
                'SELECT (esse_nome, senha) FROM esse.tb_esse where esse_nome=%s and senha=%s',
                (nome, senha))
            usuarios = cursor.fetchall()
            # print(usuarios)
            # print(type(usuarios))
            # print(len(usuarios))
            if len(usuarios) != 0:
                return 'ok'
            return 'DO NOT'
        except:
            return 'not'
