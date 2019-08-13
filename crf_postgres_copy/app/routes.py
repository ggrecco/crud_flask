from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm
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
        user = User.query.filter_by(esse_nome=form.username.data).first()
        print(user.senha)
        if user is None or user.senha != form.password.data:
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


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data,
#                     email=form.email.data,
#                     permissions='read',
#                     status='blocked')
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Parabéns você foi cadastrado com sucesso!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

# @app.route('/user/<username>')
# @login_required
# def user(username):
#     user = Tb_usuarios.query.filter_by(login=username).first_or_404()
#     return render_template('user.html', user=user)

# @app.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#     form = EditProfileForm(current_user.username, current_user.email)
#     if form.validate_on_submit():
#         current_user.username = unidecode.unidecode(form.username.data)
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('Alterações realizadas com sucesso.')
#         return redirect(url_for('index'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     return render_template('edit_profile.html',
#                            title='Edit Profile',
#                            form=form)

# @app.route("/delete_myuser/<myuser>", methods=['GET', 'POST'])
# @login_required
# def delete_myuser(myuser):
#     form = DeleteForm()
#     if form.validate_on_submit() and current_user.permissions == 'admin':
#         u = Tb_usuarios.query.filter_by(login=myuser).first()
#         # c = Coisa.query.filter_by(user_id=u.id)
#         db.session.delete(u)
#         c.delete()
#         db.session.commit()
#         flash('Usuário excluido com sucesso.')
#         return redirect(url_for('index'))
#     elif form.validate_on_submit() and current_user.permissions != 'admin':
#         user_id = int(current_user.id)
#         u = User.query.filter_by(id=user_id).first()
#         db.session.delete(u)
#         db.session.commit()
#         flash('Usuário excluido com sucesso.')
#         return redirect(url_for('logout'))
#     return render_template('delete_myuser.html',
#                            title='Excluir perfil',
#                            form=form,
#                            user=myuser)

# @app.route("/admin", methods=['GET', 'POST'])
# @login_required
# def admin():
#     u = int(current_user.id)
#     user = User.query.filter_by(id=u)
#     if user[0].permissions != 'admin':
#         return redirect(url_for('index'))
#     user = User.query.all()
#     return render_template('list_users.html', title='Usuarios', users=user)

# @app.route("/edit_user/<user>", methods=['GET', 'POST'])
# @login_required
# def edit_user(user):
#     u = User.query.filter_by(username=user).first()
#     adm = User.query.filter_by(username=current_user.username)
#     form = EditUserForm(u.username, u.email)
#     if form.validate_on_submit() and adm[0].permissions == 'admin':
#         u.username = unidecode.unidecode(form.username.data)
#         u.email = form.email.data
#         if form.permis.data != 'selecione':
#             u.permissions = form.permis.data
#         if form.status.data != 'selecione':
#             u.status = form.status.data
#         db.session.commit()
#         flash('Alterações realizadas com sucesso.')
#         return redirect(url_for('admin'))
#     elif request.method == 'GET':
#         form.username.data = u.username
#         form.email.data = u.email
#         form.status.data = u.status
#         form.permis.data = u.permissions
#     return render_template('edit_users.html', user=u, form=form)

# @app.route("/create", methods=['GET', 'POST'])
# @login_required
# def create():
#     if current_user.permissions == 'create' or 'update' or 'crud':
#         form = CoisaForm()
#         if form.validate_on_submit():
#             u = int(current_user.id)
#             coisa = Coisa(name=form.name.data,
#                           age=form.age.data,
#                           weight=form.weight.data,
#                           priority=form.priority.data,
#                           user_id=u)
#             db.session.add(coisa)
#             db.session.commit()
#             flash('Cadastro realizado com sucesso')
#             return redirect(url_for('create'))
#         return render_template('create.html',
#                                title='qualquer coisa',
#                                form=form)
#     else:
#         return render_template('404.html')

# @app.route("/read", methods=['GET', 'POST'])
# @login_required
# def read():
#     if current_user.permissions == 'create_read' or 'update' or 'crud':
#         u = int(current_user.id)
#         coisa = Coisa.query.filter_by(user_id=u)
#         size = len(list(coisa))
#         return render_template('list_data.html', size=size, coisas=coisa)
#     return render_template('404.html')

# @app.route("/update/<name>/<cid>", methods=['GET', 'POST'])
# @login_required
# def update(name, cid):
#     if current_user.permissions == 'update' or 'crud':
#         coisa = Coisa.query.filter_by(id=cid,
#                                       name=name,
#                                       user_id=current_user.id).first()
#         form = CoisaForm()
#         if form.validate_on_submit():
#             if coisa.name != form.name.data:
#                 coisa.name = form.name.data
#                 # flash('Não é permitido trocar o nome.')
#             if coisa.age != form.age.data:
#                 coisa.age = form.age.data
#             if coisa.weight != form.weight.data:
#                 coisa.weight = form.weight.data
#             if coisa.priority != form.priority.data:
#                 coisa.priority = form.priority.data
#             db.session.commit()
#             flash('Atualizado com sucesso')
#             return redirect(url_for('read'))
#         elif request.method == 'GET':
#             form.name.data = coisa.name
#             form.age.data = coisa.age
#             form.weight.data = coisa.weight
#             form.priority.data = coisa.priority
#         return render_template('edit_data.html', coisas=coisa, form=form)
#     return redirect(url_for('read'))

# @app.route("/delete/<cid>/<name>", methods=['GET', 'POST'])
# @login_required
# def delete(cid, name):
#     if current_user.permissions == 'delete' or 'crud':
#         form = DeleteForm()
#         coisa = Coisa.query.filter_by(id=cid,
#                                       name=name,
#                                       user_id=current_user.id).first_or_404()
#         if form.validate_on_submit():
#             db.session.delete(coisa)
#             db.session.commit()
#             flash('{} Excluido.'.format(name))
#             return redirect(url_for('read'))
#         return render_template('delete_date.html', form=form, coisas=coisa)
