from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField
from wtforms.validators import DataRequired

class WebsiteForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

class PageForm(FlaskForm):
    label = StringField('Label', validators=[DataRequired()])

class ContentForm(FlaskForm):
    active_status = BooleanField('Active Status', default=True)
    title = StringField('Title', validators=[DataRequired()])
    start_date = DateTimeField('Display Start Date', validators=[DataRequired()])
    end_date = DateTimeField('Display End Date')
    body_details = TextAreaField('Body Details', validators=[DataRequired()])