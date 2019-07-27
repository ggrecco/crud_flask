from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()],
                           render_kw={"placeholder": "Nome de Usuário"})
    password = PasswordField('Senha', validators=[DataRequired()],
                             render_kw={"placeholder": "Senha"})
    remember_me = BooleanField('Lembrar')
    submit = SubmitField('Entrar', render_kw={"class": "testandoCLASS",
                                              "id": "tetandoID"})



class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha',
                              validators=[DataRequired(),
                                          EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Favor utilizar outro nome de usuário.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Favor utilizar outro endereço de e-mail.')


class EditProfileForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    submit = SubmitField('Enviar')

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
    submit = SubmitField('Excluir')


class EditUserForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    status = SelectField('Status', choices=[('selecione', 'selecione'),
                                            ('active', 'Ativo'),
                                            ('blocked', 'Bloqueado')])
    permis = SelectField('Permissões',
                         choices=[('selecione', 'selecione'),
                                  ('create_read', 'Cadastrar e Visualizar'),
                                  ('update', 'Editar'),
                                  ('delete', 'Excluir'),
                                  ('crud', 'Todas'),
                                  ('admin', 'Administrador')])
    submit = SubmitField('Enviar')

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
                       render_kw={"placeholder": "Nome"})
    age = StringField('Idade', validators=[DataRequired()],
                      render_kw={"placeholder": "Idade"})
    weight = StringField('Peso', validators=[DataRequired()],
                         render_kw={"placeholder": "em Kg"})
    priority = SelectField('Prioridade', choices=[('verde', 'Verde'),
                                                  ('amarelo', 'Amarelo'),
                                                  ('vermelho', 'Vermelho')])
    submit = SubmitField('Cadastrar')
