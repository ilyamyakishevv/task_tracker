from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from tasktrackerapp.models import Users


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()],render_kw={"class": "form-control"})
    submit = SubmitField('Ввод', render_kw={"class":"btn btn-primary"})


class AddForm(FlaskForm):
    login = StringField("Логин пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()],render_kw={"class": "form-control"})
    firname_lasname = StringField("Имя пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField("E-mail пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    role = StringField("Права пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    select = SelectField("Выберите роль пользователя", choices=[])
    submit = SubmitField("Ввод", render_kw={"class":"btn btn-primary"})



class DeleteForm(FlaskForm):
    del_login = StringField("Логин удаляемого пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit2 = SubmitField("Ввод", render_kw={"class":"btn btn-primary"})

    """ class EditForm(FlaskForm):
        edit_login = StringField("Логин изменяемого пользователя", validators=[DataRequired()], render_kw={"class": "form-control"})
        firname_lasname = StringField("Имя пользователя",  render_kw={"class": "form-control"})
        email = StringField("E-mail пользователя",  render_kw={"class": "form-control"})
        role = StringField("Права пользователя",  render_kw={"class": "form-control"})
        submit = SubmitField("Изменить", render_kw={"class":"btn btn-primary"}) """


