from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager, csrf, limiter
from .models import User
from dotenv import load_dotenv
import json
# from flask_talisman import Talisman

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Talisman(app, 
    #         force_https=False, 
    #         content_security_policy=None, 
    #         session_cookie_secure=False,
    #         session_cookie_samesite='Lax'
    #     )

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' 
    login_manager.login_message_category = 'info'
    csrf.init_app(app)
    limiter.init_app(app)

    @app.template_filter('from_json')
    def from_json_filter(value):
        if isinstance(value, dict):
            return value
        
        try:
            return json.loads(value)
        
        except (ValueError, TypeError):
            return {}

    @login_manager.user_loader
    def load_user(user_id):
        print(f"DEBUG: Attempting to load user with ID: {user_id}") # Check your terminal for this!
        if user_id is None or user_id == 'None':
            return None
        try:
            user = db.session.get(User, int(user_id))
            if user:
                print(f"DEBUG: Successfully loaded {user.email}")
            else:
                print(f"DEBUG: No user found in database with ID {user_id}")
            return user
        except Exception as e:
            print(f"DEBUG: Error in load_user: {e}")
            return None

    from .routes.auth_routes import auth_bp
    from .routes.flight_routes import flight_bp
    from .routes.booking_routes import booking_bp
    from .routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(flight_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(admin_bp)

    return app