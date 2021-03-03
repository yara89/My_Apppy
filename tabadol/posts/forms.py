from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    lng = HiddenField('lng', validators=[DataRequired()])
    lat = HiddenField('lat', validators=[DataRequired()])
    location = HiddenField('location', validators=[DataRequired()])
    offers_type = SelectField(u'Type of activity',
                              choices=[('give',
                                        'need')],
                              validators=[
                                  DataRequired()
                              ])

    submit = SubmitField('Post')
