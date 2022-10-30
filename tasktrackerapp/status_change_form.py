from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  InputRequired


class StatusChange(FlaskForm):
    in_work_change = SubmitField(
        "Взять в работу",
        validators=[ InputRequired()],
        render_kw={'class': 'btn btn-primary'}
        )
    in_review_change = SubmitField(
        "Отправить на проверку",
        validators=[InputRequired()], 
        render_kw={'class': 'btn btn-primary'}
        )
    revision = SubmitField(
        "Отправить на доработку",
        validators=[InputRequired()], 
        render_kw={'class': 'btn btn-primary'}
        )
    done_change = SubmitField(
        "Одобрить и закрыть",
        validators=[InputRequired()], 
        render_kw={'class': 'btn btn-primary'}
        )
    cancelation = SubmitField(
        "Отменить задачу",
        validators=[InputRequired()], 
        render_kw={'class': 'btn btn-primary'}
        )
