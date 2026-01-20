from app.extensions import db

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), nullable=False)
    seat_number = db.Column(db.String(5), nullable=False)
    seat_type = db.Column(db.String(20)) # e.g., Window, Aisle
    price = db.Column(db.Integer)
    is_booked = db.Column(db.Boolean, default=False)
    locked_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("flight_number", "seat_number", name="unique_seat_per_flight"),
    )