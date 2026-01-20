import os

class Config:
    # SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SECRET_KEY = "DEBUG_KEY_123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///airline.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = "Lax"
    SERVER_NAME = None 
    SESSION_COOKIE_DOMAIN = None
