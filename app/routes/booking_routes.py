from flask import Blueprint, flash, redirect, render_template, request, session, url_for
import json
from datetime import datetime, timezone

from flask_login import current_user, login_required
from app.models.booking import Booking
from app.models.seat import Seat
from app.services.audit_service import log_action
from app.services.payment_service import process_payment
from app.services.seat_services import generate_seats
from app.extensions import db
# from utils.decorators import login_required
from utils.sanitize import clean_form

booking_bp = Blueprint("booking", __name__, url_prefix="/booking")

@booking_bp.route("/details", methods=["GET", "POST"])
@login_required
def flight_details():
    if request.method == "POST":
        try:
            flight_json = request.form.get("flight_data")

            print(f"DEBUG: Received Flight JSON: {flight_json}")
            
            if not flight_json:
                flash("No Flight Data found", "danger")
                return redirect(url_for("flight.search_flights_view"))
            
            flight = json.loads(flight_json)
            price = request.form.get("price")
            currency = request.form.get("currency")

            session["flight"]=flight
            session["price"]=price
            session["currency"]=currency

        except (ValueError, TypeError) as e:
            flash("Error processing flight data", "danger")
            return redirect(url_for("flight.search_flights_view"))
        
    else:
        flight=session.get("flight")
        price=session.get("price")
        currency=session.get("currency")

    if not flight:
        return redirect(url_for("flight.search_flights_view"))
    
    f_num = flight.get('itineraries')[0]['segments'][0]['number']
    seats = Seat.query.filter_by(flight_number=f_num).all()

    if not seats:
        for row in range(1, 11):
            for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
                new_seat = Seat(
                    flight_number=f_num,
                    seat_number=f"{row}{letter}",
                    is_available=True,
                    seat_type="BUSINESS" if row <= 2 else "ECONOMY",
                    price=price 
                )
                db.session.add(new_seat)
            
        db.session.commit()
        seats = Seat.query.filter_by(flight_number=f_num).all()

    return render_template(
        "select_seat.html",
        flight=flight,
        price=price,
        currency=currency,
        seats=seats
    )

@booking_bp.route("/my-bookings")
@login_required
def my_bookings_view():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).all()
    for b in user_bookings:
        if isinstance(b.flight_data, str):
            b.flight_data = json.loads(b.flight_data)

    return render_template("booking_history.html", bookings=user_bookings)

@booking_bp.route("/select-seat", methods=["GET", "POST"])
@login_required
def select_seat():
    if request.method =="POST":
        session["name"] = request.form.get("name")
        session["email"] = request.form.get("email")
        session["phone"] = request.form.get("phone")

    flight = session.get("flight")
    if not flight:
        return redirect(url_for("flight.search_flights_view"))

    seats = Seat.query.filter_by(is_booked=False).all()
    return render_template("select_seat.html", seats=seats)

@booking_bp.route("/pay", methods=["GET","POST"])
@login_required
def pay():
    if request.method == "POST":
        form_data = clean_form(request.form)
        raw_seat_id = request.form.get("seat_id")
        if not raw_seat_id:
            flash("Please select a seat before proceeding", "warning")
            return redirect(url_for("booking.flight_details"))
        session["seat_id"] = int(raw_seat_id)
        session["name"] = form_data.get("name")
        session["email"] = form_data.get("email")
        session["phone"] = form_data.get("phone")

    seat_id = session.get("seat_id")
    if not seat_id:
        return redirect(url_for("flight.search_flights_view"))
    
    seat = Seat.query.get_or_404(seat_id)

    if seat.is_booked:
        flash("That seat was just taken! Please choose another.", "danger")
        return redirect(url_for("booking.confirm_booking"))

    return render_template("payment.html", 
                           seat=seat,
                           flight=session.get("flight"),
                           price=session.get("price"),
                           currency=session.get("currency"))

@booking_bp.route("/ticket/<int:booking_id>")
@login_required
def view_ticket(booking_id):
    booking = Booking.query.filter_by(id=booking_id, user_id=current_user.id).first_or_404()
    
    # Force conversion if the database returned a string
    if isinstance(booking.flight_data, str):
        booking.flight_data = json.loads(booking.flight_data)
    
    return render_template("booking_success.html", booking=booking)

@booking_bp.route("/confirm", methods=["POST"])
@login_required
def confirm_booking():
    seat_id=session.get("seat_id")
    if not seat_id:
        return redirect(url_for("flight.search_flights_view"))
    
    seat = Seat.query.get_or_404(seat_id)
    result = process_payment(session.get('price'), session.get('currency'), request.form)

    if not result["success"]:
        flash("Payment Failure", "danger")
        return redirect(url_for("booking.pay"))

    try:
        new_booking = Booking(
            passenger_name=session.get("name"),
            passenger_email=session.get("email"),
            passenger_phone=session.get("phone"),
            seat_id=seat.id,
            flight_data=session.get("flight"),
            price=session.get("price"),
            currency=session.get("currency"),
            created_at=datetime.now(timezone.utc),
            user_id=current_user.id,
            status="CONFIRMED"
        )

        seat.is_booked=True
        db.session.add(new_booking)
        db.session.commit()

        log_action(f"BOOKING_SUCCESSFUL_ID_{new_booking.id}")
        booking_for_template = new_booking
        for key in ["flight", "price", "currency", "seat_id", "name", "email", "phone"]:
            session.pop(key, None)

        return render_template("booking_success.html", booking=booking_for_template)
    
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        flash("An error occured while saving your booking", "danger")
        return redirect(url_for("booking.pay"))

@booking_bp.route("/history")
@login_required
def history():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.login"))
    
    bookings = Booking.query.fliter_by(user_id=user_id)\
                            .order_by(Booking.created_at.desc()).all()

    return render_template("booking_history.html",bookings=bookings)