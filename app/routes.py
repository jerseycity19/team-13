import json
from app import app, bucket, db
from datetime import datetime
from firebase_admin.firestore import SERVER_TIMESTAMP
from flask import render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from os import remove
from os.path import join

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        country_file = open("app/data/country-by-continent.json")
        countries = json.load(country_file)
        language_file = open("app/data/languages.json", encoding="utf-8")
        languages = json.load(language_file)
        highlightColor = "#e2656b"
        return render_template('main.html', countries=countries, languages=languages, highlightColor=highlightColor)
    	
    # it's a POST
    to_insert = request.form.to_dict()

    if 'condition' in to_insert:
        to_insert["condition"] = True if to_insert["condition"] == 'checked' else False

    db.collection('Information').add(to_insert)

    return redirect(url_for("index")) 