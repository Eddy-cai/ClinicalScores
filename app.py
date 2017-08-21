from flask import Flask, request, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import datetime
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
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

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

@app.route('/resources/publications/')
def publications():
    return render_template('publications.html')

@app.route('/resources/ratingsystem/')
def ratingsystem():
    return render_template('ratingsystem.html')

@app.route('/resources/implementationguides/')
def implementationguides():
    return render_template('implementationguides.html')

@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/search/results/')
def results():
    return render_template('results.html')

@app.route('/search/rules/')
def rules():
    return render_template('rules.html')

@app.route('/browse/')
def browse():
    return render_template('browse.html')

@app.route('/browse/categoryresults/')
def categoryresults():
    return render_template('categoryresults.html')

@app.route('/getinvolved/')
def getinvolved():
    return render_template('getinvolved.html')

@app.route('/getinvolved/submitarule/')
def submitarule():
    return render_template('submitarule.html')

@app.route('/getinvolved/forum/')
def forum():
    return render_template('forum.html')

if __name__ == '__main__':
    app.run()
