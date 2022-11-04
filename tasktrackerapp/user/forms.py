from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,  BooleanField
from wtforms.validators import DataRequired
from tasktrackerapp.user.models import Users
from flask import flash


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()],render_kw={"class": "form-control"})
    submit = SubmitField('Ввод', render_kw={"class":"btn btn-primary"})
    remember = BooleanField('Запомнить меня', default=True, render_kw={"class":"form-check-input"})
