from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

# form for creating a new emotions entry
class EntryForm(Form):
    emotion = StringField('Emotion', validators=[DataRequired()])
