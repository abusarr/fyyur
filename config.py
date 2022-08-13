import os
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf.csrf import CSRFProtect

# rom flask_migrate import Migrate

app = Flask(__name__)
csrf = CSRFProtect(app)

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Abu195@localhost:5432/mabase3"
