from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

class OpinionForm(FlaskForm):
    title = StringField(
        'Название фильма',
        validators=[DataRequired(message='Обязательное поле'), Length(min=1, max=128)]
    )
    text = TextAreaField(
        'Ваше мнение',
        validators=[DataRequired(message='Обязательное поле')]
    )
    source = URLField(
        'Ссылка на обзор (необязательно)',
        validators=[Length(min=1, max=256), Optional()]
    )
    submit = SubmitField('Добавить')