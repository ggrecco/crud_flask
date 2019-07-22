from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()],
                            render_kw={"placeholder" : "Nome de Usuário"})
    password = PasswordField('Senha', validators=[DataRequired()],
                            render_kw={"placeholder" : "Senha"})
    remember_me = BooleanField('Lembrar')
    submit = SubmitField('Entrar', render_kw={"class": "testandoCLASS", "id": "tetandoID"})
    # escolhas = SelectField('Escolha', choices=[('escolha 1', 'escolha 1'),
    #                                             ('escolha 2', 'escolha 2'),
    #                                             ('escolha 3', 'escolha 3')],
    #                        render_kw={"class": "teste"})


class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Repita a senha', validators=[DataRequired(), EqualTo('password')])
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

    # verifica usuario e e-mail no banco de dados
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

        def validate_username(self, username):
            if username.data != self.original_username:
                user = User.query.filter_by(username=self.username.data).first()
                if user is not None:
                    raise ValidationError('Favor utilizar outro nome de usuario.')

    def __init__(self, original_email, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_email = original_email

        def validate_email(self, email):
            if email.data != self.original_email:
                email = User.query.filter_by(email=self.email.data).first()
                if email is not None:
                    raise ValidationError('Favor utilizar outro e-mail.')


class DelForm(FlaskForm):
    submit = SubmitField('Excluir')