from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, DeleteForm
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime
from flask import g
from flask_babel import get_locale, _
import unidecode


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@app.route('/')
@app.route('/index')
@login_required
def index():
    msg = {'frase': 'crud-flask'}
    return render_template('olacrud.html', title='Crud-Flask', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data) or user.status != 'ativo':
            flash(_('Invalid user or password'))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    permissions='ler', status='ativo')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabéns você foi cadastrado com sucesso!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.username = unidecode.unidecode(form.username.data)
        current_user.email = form.email.data
        db.session.commit()
        flash('Alterações realizadas com sucesso.')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route("/delete_myuser/<myuser>", methods=['GET', 'POST'])
@login_required
def delete_myuser(myuser):
    form = DeleteForm()
    if form.validate_on_submit() and current_user.permissions == 'admin':
        print('sou admin')
        u = User.query.filter_by(username=myuser).first()
        db.session.delete(u)
        db.session.commit()
        flash('Usuário excluido com sucesso.')
        return redirect(url_for('index'))
    elif form.validate_on_submit() and current_user.permissions != 'admin':
        user_id = int(current_user.id)
        u = User.query.filter_by(id=user_id).first()
        db.session.delete(u)
        db.session.commit()
        flash('Usuário excluido com sucesso.')
        return redirect(url_for('logout'))
    return render_template('delete_myuser.html', title='Excluir perfil',
                           form=form, user=myuser)


@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    u = int(current_user.id)
    user = User.query.filter_by(id=u)
    if user[0].permissions != 'admin':
        return redirect(url_for('index'))
    user = User.query.all()
    return render_template('list_users.html', title='Usuarios', 
                            users=user)


@app.route("/bloq/<user>/<status>", methods=['GET', 'POST'])
@login_required
def bloq(user, status):
    u = User.query.filter_by(username=user).first()
    adm = User.query.filter_by(username=current_user.username)
    if adm[0].permissions == 'admin':
        u.status = status
        db.session.commit()
    return redirect(url_for('admin'))