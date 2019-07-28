from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()],
                           render_kw={"placeholder": "Nome de Usuário",
                                      "class": "form"})
    password = PasswordField('Senha', validators=[DataRequired()],
                             render_kw={"placeholder": "Senha",
                                        "class": "form"})
    remember_me = BooleanField('Lembrar')
    submit = SubmitField('Entrar', render_kw={"class": "btn-blue"})


class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()],
                           render_kw={"class": "form"})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={"class": "form"})
    password = PasswordField('Senha', validators=[DataRequired()],
                             render_kw={"class": "form"})
    password2 = PasswordField('Repita a senha',
                              validators=[DataRequired(),
                                          EqualTo('password')],
                              render_kw={"class": "form"})
    submit = SubmitField('Registrar', render_kw={"class": "btn-blue"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Favor utilizar outro nome de usuário.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Favor utilizar outro endereço de e-mail.')


class EditProfileForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()],
                           render_kw={"class": "form"})
    email = StringField('E-mail', validators=[DataRequired()],
                        render_kw={"class": "form"})
    submit = SubmitField('Enviar', render_kw={"class": "btn-blue"})

    def __init__(self, original_username, original_email, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            raise ValidationError('Favor utilizar outro nome de usuario.')

    def validate_email(self, email):
        if email.data != self.original_email:
            email = User.query.filter_by(email=self.email.data).first()
            if email is not None:
                raise ValidationError('Favor utilizar outro e-mail.')


class DeleteForm(FlaskForm):
    submit = SubmitField('Excluir', render_kw={"class": "btn-red"})


class EditUserForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()],
                           render_kw={"class": "form"})
    email = StringField('E-mail', validators=[DataRequired()],
                        render_kw={"class": "form"})
    status = SelectField('Status',
                         choices=[('selecione', 'selecione'),
                                  ('active', 'Ativo'),
                                  ('blocked', 'Bloqueado')],
                         render_kw={"class": "form"})
    permis = SelectField('Permissões',
                         choices=[('selecione', 'selecione'),
                                  ('create_read', 'Cadastrar e Visualizar'),
                                  ('update', 'Cadastrar, Visualizar e Editar'),
                                  ('delete', 'Excluir'),
                                  ('crud', 'Todas'),
                                  ('admin', 'Administrador')],
                         render_kw={"class": "form-dropdown"})
    submit = SubmitField('Enviar', render_kw={"class": "btn-blue"})

    def __init__(self, original_username, original_email, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Favor utilizar outro nome de usuario.')

    def validate_email(self, email):
        if email.data != self.original_email:
            email = User.query.filter_by(email=self.email.data).first()
            if email is not None:
                raise ValidationError('Favor utilizar outro e-mail.')


class CoisaForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()],
                       render_kw={"placeholder": "Nome",
                                  "class": "form"})
    age = StringField('Idade', validators=[DataRequired()],
                      render_kw={"placeholder": "Idade",
                                 "class": "form"})
    weight = StringField('Peso', validators=[DataRequired()],
                         render_kw={"placeholder": "em Kg",
                                    "class": "form"})
    priority = SelectField('Prioridade',
                           choices=[('verde', 'Verde'),
                                    ('amarelo', 'Amarelo'),
                                    ('vermelho', 'Vermelho')],
                           render_kw={"class": "form form-dropdown"})
    submit = SubmitField('Cadastrar',
                         render_kw={"class": "btn-blue"})
