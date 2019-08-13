from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
    __table_args__ = {'schema': 'esse'}
    __tablename__ = 'tb_esse'
    id = db.Column(db.Integer, primary_key=True)
    esse_nome = db.Column(db.String())
    senha = db.Column(db.String())

    def __repr__(self):
        return '<Usuario {}>'.format(self.esse_nome)

    def set_password(self, senha):
        print(senha)
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        print(senha)
        return check_password_hash(self.senha, senha)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))