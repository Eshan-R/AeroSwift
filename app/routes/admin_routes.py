from flask import Blueprint, render_template, redirect, url_for
from app.models.booking import Booking
from sqlalchemy import func
from app.extensions import db
from app.services.audit_service import log_action
from app.models.audit_log import AuditLog
from utils.decorators import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
@admin_required
def dashboard():
    return render_template("admin_dashboard.html")

@admin_bp.route("/bookings")
@admin_required
def all_bookings():
    bookings = Booking.query.order_by(Booking.created_at.desc()).all()
    return render_template("admin_bookings.html", bookings=bookings)

@admin_bp.route("/stats")
@admin_required
def stats():
    total_bookings = Booking.query.count()
    total_revenue = db.session.query(func.sum(Booking.price)).scalar() or 0

    confirmed = Booking.query.filter_by(status="CONFIRMED").count()
    pending = Booking.query.filter_by(status="PENDING").count()

    return render_template(
        "admin_stats.html",
        total_bookings=total_bookings,
        total_revenue=total_revenue,
        confirmed=confirmed,
        pending=pending
    )

@admin_bp.route("/cancel/<int:booking_id>")
@admin_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    if booking.seat:
        booking.seat.is_booked = False

    booking.status = "CANCELLED"
    log_action(f"BOOKING_CANCELLED:{booking.id}")
    db.session.commit()

    return redirect(url_for("admin.all_bookings"))

@admin_bp.route("/logs")
@admin_required
def view_logs():
    logs = AuditLog.query.order_by(AuditLog.created_at.desc()).limit(200).all()
    return render_template("admin_logs.html", logs=logs)