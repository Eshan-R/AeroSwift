from app.extensions import db

class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    city = db.Column(db.String(100), nullable = False)
    country = db.Column(db.String(100), nullable = False)

    __table_args__ = (db.Index('idx_airport_code', 'code'),)