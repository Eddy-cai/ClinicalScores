from flask import Flask, request, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

import os



BASEDIR = os.path.abspath(os.path.dirname(__file__))

# create app
app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutus/')
def aboutus():
    return render_template('aboutus.html')

@app.route('/aboutus/ourteam/')
def ourteam():
    return render_template('ourteam.html')

@app.route('/aboutus/ourservices/')
def ourservices():
    return render_template('ourservices.html')

@app.route('/aboutus/contactus/')
def contactus():
    return render_template('contactus.html')

@app.route('/resources/')
def resources():
    return render_template('resources.html')


@app.route('/resources/publications')
def publications():
    return render_template('publications.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
