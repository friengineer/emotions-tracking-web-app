from app import db

# model for emotions and stress data in the database
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.String(500))
