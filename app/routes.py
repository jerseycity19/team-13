from flask import render_template
from app import app
import json

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    country_file = open("app/data/country-by-continent.json")
    countries = json.load(country_file)
    language_file = open("app/data/languages.json", encoding="utf-8")
    languages = json.load(language_file)
    return render_template('main.html', countries=countries, languages=languages)

