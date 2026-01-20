from app.extensions import db
from app.models.seat import Seat

def generate_seats(flight_number):
    existing = Seat.query.filter_by(flight_number=flight_number).first()
    if existing:
        return

    seats = []

    for row in range(1, 21):
        for col in  ["A", "B", "C", "D", "E", "F"]:
            seat_type = "middle"
            price = 0

            if col in ["A", "F"]: # Window Seats
                seat_type = "window"
                price = 500
            elif col in ["C", "D"]:
                seat_type = "aisle"
                price = 300

            if row <= 3:
                seat_type = "extra_legroom"
                price = 1000

            seats.append(Seat(
                flight_number=flight_number,
                seat_number=f"{row}{col}",
                seat_type=seat_type,
                price=price
            ))

    db.session.bulk_save_objects(seats)
    db.session.commit()