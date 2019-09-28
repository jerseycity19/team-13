from flask import render_template
from app import app
import json

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

@app.route('/languages')
def languages():
    language_file = open("app/data/languages.json")
    languages = json.load(language_file)
    return render_template('languages.html', languages=languages)