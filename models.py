import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy, db
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from config import csrf
from wtforms.csrf.core import CSRF
#from flask_migrate import Migrate
import sys

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Abu195@localhost:5432/fyyur'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Venue(db.Model):
    __tablename__ = "venue"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(300), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120), nullable=False)
    shows = db.relationship("Show", backref="venue", lazy=False)

    def __repr__(self):
        return f"<Venue: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, address: {self.address}, phone: {self.phone}, image_link: {self.image_link}, facebook_link: {self.facebook_link}, genres: {self.genres}, website: {self.website}, shows: {self.shows}>"


class Artist(db.Model):
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(300), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    shows = db.relationship("Show", backref="artist", lazy=False)

    def __repr__(self):
        return f"<Artist: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, phone: {self.phone}, genres: {self.genres}, image_link: {self.image_link}, facebook_link: {self.facebook_link}, shows: {self.shows}>"


class Show(db.Model):
    _tablename__ = "show"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)

    def __repr__(self):
        return f"<Show {self.id}, date: {self.date}, artist_id: {self.artist_id}, venue_id: {self.venue_id}>"
