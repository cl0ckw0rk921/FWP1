"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FWP1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
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

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Me',
        year=datetime.now().year,
        message='Meet the One(s) Behind the Scenes'
    )
