from flask_wtf import FlaskForm
from wtf import StringField, SubmitField
from wtf.validators import DataRequired, Length, Email

class ContactForm(FlaskForm)
    name = StringField('Name', validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    message = StringField('Your Message', validators = [DataRequired(), Length(min=2, max=150)])
    submit = SubmitField('Submit')