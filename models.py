from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SpeedTestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latency = db.Column(db.Float, nullable=False)
    jitter = db.Column(db.Float, nullable=False)
    down_100kbps = db.Column(db.Float, nullable=False)
    down_1mbps = db.Column(db.Float, nullable=False)
    down_10mbps = db.Column(db.Float, nullable=False)
    down_25mbps = db.Column(db.Float, nullable=False)
    up_100kbps = db.Column(db.Float, nullable=False)
    up_1mbps = db.Column(db.Float, nullable=False)
    up_10mbps = db.Column(db.Float, nullable=False)
    percentile_down = db.Column(db.Float, nullable=False)
    percentile_up = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
