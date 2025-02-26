from dotenv import load_dotenv
import os
load_dotenv()

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Set a default secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')  # Fallback to SQLite if missing

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

