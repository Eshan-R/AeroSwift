from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.extensions import db, limiter
from app.models.user import User
from utils.sanitize import clean_form
from flask_login import login_user, logout_user, current_user
from app.services.audit_service import log_action

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("flight.home"))
    
    if request.method == "POST":
        data = clean_form(request.form)
        email = data.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user, remember=True)
            session.permanent = True
            
            log_action("LOGIN_SUCCESS", user_id=user.id)
            
            next_page = request.args.get('next')
            return redirect(next_page or url_for("flight.home"))

        log_action("LOGIN_FAILURE", email=email)
        flash("Invalid email or password", "danger")         

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("flight.home"))

    if request.method == "POST":
        data = clean_form(request.form)

        email = data.get("email")

        if User.query.filter_by(email=email).first():
            log_action("REGISTER_DUPLICATE", email=email)
            flash("Email already registered", "warning")
            return redirect(url_for("auth.register"))

        user = User(
            name=data.get("name"),
            email=email
        )
        user.set_password(request.form["password"])

        db.session.add(user)
        db.session.commit()

        log_action("REGISTER_SUCCESS", user_id=user.id)
        flash("Account created successfully")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    if current_user.is_authenticated:
        log_action("LOGOUT", user_id=current_user.id)
    
    logout_user()
    session.clear()
    flash("Logged out successfully", "info")
    return redirect(url_for("auth.login"))