import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_DRIVE = os.getenv("DB_DRIVE")
    DB_CONTROLLER = os.getenv("DB_CONTROLLER")
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")

    SQLALCHEMY_DATABASE_URI = f"{DB_DRIVE}+{DB_CONTROLLER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
