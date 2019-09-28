from app import app, bucket, db, partners, users
from flask import render_template, request, url_for, redirect, session
import json


@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    code = request.args.get('code')
    if request.method == 'GET':
        country_file = open("app/data/country-by-continent.json")
        countries = json.load(country_file)
        language_file = open("app/data/languages.json", encoding="utf-8")
        languages = json.load(language_file)

        highlightColor = "#e2656b"
        event = db.collection('events').document(code).get().to_dict()

        if event:
            highlightColor = event['fgcolor']

        return render_template('main.html', countries=countries,
                               languages=languages, code=code,
                               highlightColor=highlightColor)

    # it's a POST
    to_insert = request.form.to_dict()
    to_insert['tag'] = code

    if 'condition' in to_insert:
        to_insert["condition"] = True if to_insert["condition"] == 'checked' else False

    db.collection('Information').add(to_insert)

    url = url_for('index')
    if code:
        url += '?code=' + code
    session['back_link'] = url

    return redirect(url_for("thanks"))

@app.route("/thank-you")
def thanks():
    url = session['back_link']
    return render_template("thank-you.html", back_link=url)
