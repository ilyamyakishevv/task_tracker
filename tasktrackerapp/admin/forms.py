from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from tasktrackerapp.user.models import Users
from flask import flash


class AddForm(FlaskForm):
    login = StringField("Логин пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()],render_kw={"class": "form-control"})
    firname_lasname = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField("E-mail пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    role = SelectField("Выберете роль пользователя")
    submit = SubmitField("Ввод", render_kw={"class":"btn btn-primary"})


class DeleteForm(FlaskForm):
    del_login = StringField("Логин удаляемого пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit2 = SubmitField("Ввод", render_kw={"class":"btn btn-primary"})
