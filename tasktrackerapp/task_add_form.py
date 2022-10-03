from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class TaskAdd(FlaskForm):
    name = StringField("Название задачи", validators=[DataRequired()])
    description = StringField("Описание задачи", validators=[DataRequired()])
    status = StringField(default='IN WORK')
    deadline = DateTimeField("Срок исполнения до", validators=[DataRequired()])
    submit = SubmitField("Создать задачу")
