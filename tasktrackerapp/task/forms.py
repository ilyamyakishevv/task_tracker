from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField, SelectField, HiddenField
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

    deadline = DateField(
        "Срок исполнения до",
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    edit = SubmitField(
        "Изменить задачу",
        render_kw={'class': 'btn btn-primary'}
        )


class CommentForm(FlaskForm):
    task_id = HiddenField('ID новости', validators=[DataRequired()])
    comment_text = StringField('Ваш комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
