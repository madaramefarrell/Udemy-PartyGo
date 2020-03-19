from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateTimeField, FloatField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed


class BasicPartyorm(FlaskForm):
    name = StringField('Party name', validators=[validators.DataRequired(), validators.Length(min=2, max=80)])
    gplace = StringField('Google Place API')
    place = StringField('Place', validators=[validators.DataRequired()], widget=TextArea())
    lng = FloatField('Longitude', validators=[validators.Optional()])
    lat = FloatField('Latitude', validators=[validators.Optional()])
    start_datetime = DateTimeField('Start time',
                                   validators=[validators.DataRequired()],
                                   format='%Y-%m-%d %H:%M')
    end_datetime = DateTimeField('End time',
                                 validators=[validators.DataRequired()],
                                 format='%Y-%m-%d %H:%M')
    description = StringField('Description ',
                              widget=TextArea(), validators=[validators.Length(min=50)])


class EditPartyForm(BasicPartyorm):
    photo = FileField('Party photo',
                      validators=[
                          FileAllowed(['jpg', 'jpeg', 'png', 'gif', ], 'Only allow .jpg .jpeg .png and .gif files')])


class CancelPartyForm(FlaskForm):
    confirm = StringField('Are you sure you want to cancel this party?', validators=[validators.DataRequired()])
