
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Project_N1_HL import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
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
        title='Short Description',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/education')
def education():
    """Renders the home page."""
    return render_template(
        'education.html',
        title='Education',
        year=datetime.now().year,
    )
@app.route('/skillset')
def skillset():
    """Renders the home page."""
    return render_template(
        'skillset.html',
        title='Skills',
        year=datetime.now().year,
    )

@app.route('/projects')
def projects():
    """Renders the home page."""
    return render_template(
        'projects.html',
        title='Projects Handeled',
        year=datetime.now().year,
    )

@app.route('/newprojects')
def newprojects():
    """Renders the home page."""
    return render_template(
        'newprojects.html',
        title='Projects to be handeled',
        year=datetime.now().year,
    )