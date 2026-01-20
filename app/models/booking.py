from datetime import datetime, timezone
from app.extensions import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passenger_name = db.Column(db.String(100))
    passenger_email = db.Column(db.String(120))
    passenger_phone = db.Column(db.String(50))
    
    seat_id = db.Column(db.Integer, db.ForeignKey("seat.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    flight_data = db.Column(db.JSON, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), default="PENDING")
    created_at = db.Column(db.DateTime, default=lambda:datetime.now(timezone.utc))

    user = db.relationship("User", backref="my_bookings")
    seat = db.relationship("Seat")