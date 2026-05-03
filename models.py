from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StrengthLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(200))
    date = db.Column(db.DateTime, nullable=False)

class CardioLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardio_type = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(200))
    date = db.Column(db.DateTime, nullable=False)