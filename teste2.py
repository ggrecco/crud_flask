from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5433/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Usuarios(db.Model):
    # __tablename__ = db.Model.metadata.tables['tb_usuarios']
    __table_args__ = {'schema': 'conf'}
    id = db.Column('id', db.Integer, primary_key=True)
    # login = db.column('login', db.Integer)


from sqlalchemy.orm import scoped_session, sessionmaker, Query
db_session = scoped_session(sessionmaker(bind=app))

for item in db_session.query(Usuarios.id):
    print(item)