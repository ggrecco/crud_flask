from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5433/teste'
db = SQLAlchemy(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()