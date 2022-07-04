# this is the file where all routes are made
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# route is for home


@views.route('/')
def base():
    return render_template("base.html")

@views.route('/')
def home():
    return render_template("home.html")
