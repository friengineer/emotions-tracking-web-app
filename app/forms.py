from flask_wtf import Form
from wtforms import widgets, SelectMultipleField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
# need to import models so emotion options can be rdefined

# creates the multiple checkboxes for emotions
class EmotionsField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# creates the multiple checkboxes for reasons for stress
class StressField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# form for creating a new emotions and stress entry
class EntryForm(Form):
    emotionsList = ['Sad\nLonely\nAngry\nDepressed\nConfused\nAnxious\nStressed\nTired']
    stressList = ['Imminent deadlines\nLack of sleep\nLots of work\nLack of attention\nLack of socialisation\nNot eating properly\nI do not know']
    list_of_emotions = emotionsList[0].split("\n")
    list_of_stress = stressList[0].split("\n")
    # all_emos = models.Emotions.query.all()
    # emotionsOptions = [(emo.id, emo.name) for emo in all_emos]
    emotionsOptions = [(i,i) for i in list_of_emotions]
    stressOptions = [(i,i) for i in list_of_stress]

    emotions = EmotionsField('Emotions', choices=emotionsOptions, validators=[DataRequired()])
    stress = StressField('Stress', choices=stressOptions, validators=[DataRequired()])
    comments = TextAreaField('Comments')
