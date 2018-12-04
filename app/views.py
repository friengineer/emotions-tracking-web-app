from flask import render_template, flash
from app import app
from .forms import EntryForm

# default route for viewing all tasks
@app.route('/')
def base():
    # entires = getEntries(2)

    # form data is only submitted if it is valid
    # if form.validate_on_submit():
        # try block tests if the task has been marked as finished and if it has a success message is
        # displayed and if not, an error message is displayed
        # try:
            # completeTask(form.number.data)
            # flash('The task has been marked as finished.')
        # except:
            # flash("An error occurred and the task was not marked as finished.")

    # renders the 'all.html' page instead of 'base.html' to incorporate the features needed for
    # displaying tasks and marking tasks as finished
    return render_template('entries.html')

# route for viewing incomplete tasks
@app.route('/create', methods=['GET', 'POST'])
def create():
    form = EntryForm()

    # form data is only submitted if it is valid
    if form.validate_on_submit():
        # try block tests if the task has been marked as finished and if it has a success message is
        # displayed and if not, an error message is displayed
        try:
            submitEntry(form.emotion.data)
            flash('The entry has been created.')
        except:
            flash('An error occurred and the entry was not created.')

    return render_template('create.html',
                           form=form)

# this function adds the data about the new emotion entry to the database
def submitEntry(emotion):
    from app import db, models
    import datetime

    newEntry = models.Entry(emotion=emotion)
    db.session.add(newEntry)
    db.session.commit()
