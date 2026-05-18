from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    risk_level = db.Column(db.String(20), nullable=False)
    reason = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=True)
    long = db.Column(db.Float, nullable=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())