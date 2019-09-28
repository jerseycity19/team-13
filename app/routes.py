from flask import render_template
from app import app
import json

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    UserID = ['Scholar', 'Student', 'Administrator', 'Non-University']
    # return render_template('test.html', UserID=UserID)
    return "Hello World"

@app.route('/languages')
def languages():
    language_file = open("app/data/languages.json")
    languages = json.load(language_file)
    return render_template('languages.html', languages=languages)

@app.route('/countries')
def countries():
    country_file = open("app/data/country-by-continent.json")
    countries = json.load(country_file)
    return render_template('countries.html', countries=countries)
