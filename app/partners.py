from app import app, bucket, db
from datetime import datetime
from firebase_admin.firestore import SERVER_TIMESTAMP
from flask import render_template, request
from werkzeug.utils import secure_filename
from os import remove
from os.path import join


def datestr_to_datetime(date_string):
    if not date_string:
        return None
    return datetime(*map(int, date_string.split('-')))


@app.route('/partners', methods=['GET', 'POST'])
def partners():
    if request.method == 'GET':
        return render_template('partner.html')

    # it's a POST
    to_insert = request.form.to_dict()
    to_insert['timestamp'] = SERVER_TIMESTAMP
    to_insert['datestart'] = datestr_to_datetime(to_insert['datestart'])
    to_insert['dateend'] = datestr_to_datetime(to_insert['dateend'])

    print(request.files.to_dict())
    if 'logo' in request.files:
        file = request.files['logo']
        if file.filename != '':
            filename = secure_filename(file.filename)
            fs_loc = join(app.config['UPLOAD_FOLDER'], filename)
            file.save(fs_loc)
            to_insert['filename'] = filename
            bucket.blob(filename).upload_from_filename(fs_loc)
            remove(fs_loc)

    event_ref = db.collection('events').document(to_insert['code'])
    event_ref.set(to_insert)
    return render_template('partner_success.html', data=request.form.to_dict())
