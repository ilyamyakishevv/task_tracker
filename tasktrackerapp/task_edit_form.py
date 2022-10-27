from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class TaskEdit(FlaskForm):
    name = StringField(
        "Название задачи",
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    description = TextAreaField(
        "Описание задачи",
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    status = SelectField("Статус задачи")

    deadline = DateField(
        "Срок исполнения до",
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    edit = SubmitField(
        "Изменить задачу",
        validators=[DataRequired()],
        render_kw={'class': 'btn btn-primary'}
        )
