from pydoc import render_doc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class TaskAdd(FlaskForm):
    name = StringField("Название задачи", validators=[DataRequired()], render_kw={'class':'form-control'})
    description = StringField("Описание задачи", validators=[DataRequired()], render_kw={'class':'form-control'})
    #status = StringField(default='IN WORK', render_kw={'class':'form-control'})
    deadline = StringField("Срок исполнения до", validators=[DataRequired()], render_kw={'class':'form-control'})
    submit = SubmitField("Создать задачу", render_kw={'class':'btn btn-primary'})
