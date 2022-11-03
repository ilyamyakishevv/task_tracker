from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from tasktrackerapp.models import Users
from flask import flash


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()],render_kw={"class": "form-control"})
    submit = SubmitField('Ввод', render_kw={"class":"btn btn-primary"})
    remember = BooleanField('Запомнить меня', default=True, render_kw={"class":"form-check-input"})


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

class CommentForm(FlaskForm):
    task_id = HiddenField('ID новости', validators=[DataRequired()])
    comment_text = StringField('Ваш комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class":"btn primary"})



