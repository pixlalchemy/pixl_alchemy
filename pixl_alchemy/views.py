from pixl_alchemy import app
from flask import url_for, render_template


@app.route('/')
def index():
    return render_template('index.html',
                           title='Home',
                           index='index')


@app.route('/about')
def about():
    return render_template('about.html',
                           title='About',
                           about='about')


@app.route('/contact')
def contact():
    return render_template('contact.html',
                           title='Contact',
                           contact='contact')


@app.route('/templates')
def templates():
    return render_template('templates.html',
                           title='Templates',
                           templates='templates')
