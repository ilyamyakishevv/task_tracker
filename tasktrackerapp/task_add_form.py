from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class TaskAdd(FlaskForm):
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
    status = StringField(
        default='OPEN',
        render_kw={'class': 'form-control'}
        )
    deadline = DateField(
        "Срок исполнения до",
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    responsible = SelectField("Исполнитель задачи")
    submit = SubmitField(
        "Создать задачу",
        render_kw={'class': 'btn btn-primary'}
        )
    
    edit = SubmitField(
        "Изменить задачу",
        render_kw={'class': 'btn btn-primary'}
        )
