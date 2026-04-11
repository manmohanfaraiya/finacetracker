import os

class Config:
    # Secret key (session ke liye)
    SECRET_KEY = "secret123"

    # SQLite Database URL
    SQLALCHEMY_DATABASE_URI = "sqlite:///finance.db"

    # Track modifications off (performance ke liye)
    SQLALCHEMY_TRACK_MODIFICATIONS = False