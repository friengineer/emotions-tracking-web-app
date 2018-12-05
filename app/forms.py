from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

# form for creating a new emotions entry
class EntryForm(Form):
    emotion = StringField('Emotion', validators=[DataRequired()])

# form for updating an entry
class UpdateForm(Form):
    number = IntegerField('Number', validators=[DataRequired()])
    emotion = StringField('Emotion', validators=[DataRequired()])
