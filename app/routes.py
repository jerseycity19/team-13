import json
from app import app, bucket, db
from flask import render_template, request, url_for, redirect


@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        country_file = open("app/data/country-by-continent.json")
        countries = json.load(country_file)
        language_file = open("app/data/languages.json", encoding="utf-8")
        languages = json.load(language_file)

        highlightColor = "#e2656b"
        code = request.args.get('code')
        event = db.collection('events').document(code).get().to_dict()

        if event:
            highlightColor = event['fgcolor']

        return render_template('main.html', countries=countries,
                               languages=languages,
                               highlightColor=highlightColor)

    # it's a POST
    to_insert = request.form.to_dict()

    if 'condition' in to_insert:
        to_insert["condition"] = True if to_insert["condition"] == 'checked' else False

    db.collection('Information').add(to_insert)

    return redirect(url_for("index"))
