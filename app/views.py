from flask import render_template, flash
from app import app
from .forms import EntryForm, UpdateForm

# default route for viewing all entries
@app.route('/', methods=['GET', 'POST'])
def base():
    entries = getEntries()
    form = UpdateForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tests if the task has been marked as finished and if it has a success message is
        # displayed and if not, an error message is displayed
        try:
            updateEntry(form.number.data, form.emotion.data)
            flash('The entry has been updated.')
        except:
            flash('An error occurred and the entry was not updated.')

    # renders the 'entries.html' page instead of 'base.html' to incorporate the features needed for
    # displaying and updating entries
    return render_template('entries.html',
                           entries=entries,
                           form=form)

# route for creating a new entry
@app.route('/create', methods=['GET', 'POST'])
def create():
    form = EntryForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tries to add the entry to the database and if it is successful a  message is
        # displayed and if not, an error message is displayed
        try:
            submitEntry(form.emotion.data)
            flash('The entry has been created.')
        except:
            flash('An error occurred and the entry was not created.')

    return render_template('create.html',
                           form=form)

# this function retrieves the emotion entries from the database
def getEntries():
    from app import db, models

    return models.Entry.query.all()

# this function updates the value of the specified emotion entry
def updateEntry(number, emotion):
    from app import db, models

    entry = models.Entry.query.get(number)
    entry.emotion = emotion
    db.session.commit()

# this function adds the data about the new emotion entry to the database
def submitEntry(emotion):
    from app import db, models

    newEntry = models.Entry(emotion=emotion)
    db.session.add(newEntry)
    db.session.commit()
