from app import db

# model for emotions and stress data in the database
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    emotions = db.Column(db.List)
    stress = db.Column(db.List)
    comments = db.Column(db.String(500))

# model for emotions in the database
class Emotions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    # new_entry.emotions = models.Emotions.filter_by(id=[])

# model for reasons for stress in the database
# class Stress(db.Model):
#     deadlines = 'Imminent deadlines'
#     sleep = 'Lack of sleep'
#     work = 'Lots of work'
#     attention = 'Lack of attention'
#     socialisation = 'Lack of socialisation'
#     eating = 'Not eating properly'
#     unsure = 'I do not know'
