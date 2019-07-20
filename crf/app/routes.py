from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    inicio = {'frase': 'crud-flask'}
    return render_template('index.html', title='Crud-Flask', inicio=inicio)