from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

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
