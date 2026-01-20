from flask import Blueprint, render_template, request
from app.services.amadeus_service import search_flights

flight_bp = Blueprint("flight", __name__)

@flight_bp.route("/")
def home():
    return render_template("home.html")

@flight_bp.route("/search", methods=["GET", "POST"])
def search_flights_view():
    flights = []

    if request.method == "POST":
        dep = request.form.get("departure")
        arr = request.form.get("arrival")
        date = request.form.get("date")
        adults = int(request.form.get("adults", 1))
        children = int(request.form.get("children", 0))
        infants = int(request.form.get("infants", 0))

        # Amadeus API Call
        flights = search_flights(dep.upper(), arr.upper(), date, adults, children, infants)

    return render_template("search_flights.html", flights=flights)
