from flask import render_template
from app import app
import json

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    UserID = ['Scholar', 'Student', 'Administrator', 'Non-University']
    return render_template('test.html', UserID=UserID)

@app.route('/languages')
def languages():
    language_file = open("app/data/languages.json", encoding="utf-8")
    languages = json.load(language_file)
    return render_template('languages.html', languages=languages)