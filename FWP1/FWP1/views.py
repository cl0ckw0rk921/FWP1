"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FWP1 import app

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Me',
        year=datetime.now().year,
        #message='Meet the One(s) Behind the Scenes'
    )

@app.route('/biographies')
def biographies():
    """Renders the biographies page."""
    return render_template(
        'biographies.html',
        title='Biographies',
        year=datetime.now().year,
        message='Your biographies page.'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact Us',
        year=datetime.now().year,
        message='Your way to get in touch with us.'
    )

@app.route('/diy')
def diy():
    """Renders the diy page."""
    return render_template(
        'diy.html',
        title='Doing it Yourself',
        year=datetime.now().year,
        message='Your diy page.'
    )

@app.route('/donations')
def donations():
    """Renders the donations page."""
    return render_template(
        'donations.html',
        title='donations',
        year=datetime.now().year,
        message='Your donations page.'
    )

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/internships')
def internships():
    """Renders the internships page."""
    return render_template(
        'internships.html',
        title='Internships',
        year=datetime.now().year,
        message='Your internships page.'
    )

@app.route('/logistics')
def logistics():
    """Renders the logistics page."""
    return render_template(
        'logistics.html',
        title='Logistics',
        year=datetime.now().year,
        message='Your page for tracking inventory.'
    )

@app.route('/sponsors')
def sponsors():
    """Renders the sponsors page."""
    return render_template(
        'sponsors.html',
        title='Sponsors',
        year=datetime.now().year,
        message='Your sponsors page.'
    )

@app.route('/volunteer')
def volunteer():
    """Renders the volunteer page."""
    return render_template(
        'volunteer.html',
        title='Volunteer',
        year=datetime.now().year,
        message='Your volunteer page.'
    )