from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)
# conexão com banco de dados
db = 'postgresql://postgres:123@localhost:5433/teste'
conn = psycopg2.connect(db)
cursor = conn.cursor()
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please login to access this page.')
moment = Moment(app)
babel = Babel(app)

from app import routes, models, errors


@babel.localeselector
def get_locale():
    return 'pt'
