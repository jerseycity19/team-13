from app import app, db
from flask import render_template, redirect, request, session, url_for
from firebase_admin.firestore import SERVER_TIMESTAMP

roles = {
    1: 'Administrator',
    2: 'Partner',
}


@app.route('/users')
def users():
    _users = db.collection('users').stream()
    users = {}

    for user in _users:
        u = user.to_dict()
        u['role'] = roles[u['role']]
        users[user.id] = u

    return render_template('users.html', users=users)


@app.route('/user_add', methods=['GET', 'POST'])
def user_add():
    if request.method == 'GET':
        return render_template('user_add.html')

    # it's a POST
    to_insert = request.form.to_dict()
    to_insert['created'] = SERVER_TIMESTAMP
    to_insert['role'] = int(to_insert['role'])
    to_insert['createdby'] = session['user']['username']

    user_ref = db.collection('users').document(to_insert['username'])
    user_ref.set(to_insert)

    session['message'] = 'Successfully modified user.'
    return redirect(url_for('users'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'message' in session:
            return render_template('login.html', message=session['message'])
        else:
            return render_template('login.html')

    # it's a POST
    to_verify = request.form.to_dict()
    candidate = db.collection('users').document(to_verify['username']).get().to_dict()
    if candidate:
        if to_verify['password'] == candidate['password']:
            if 'message' in session:
                del session['message']

            session['user'] = candidate
            if candidate['role'] == 2:  # partner
                return redirect(url_for('partners'))
            elif candidate['role'] == 1:  # admin
                return redirect(url_for('users'))

    session['message'] = 'Authentication failed.'
    return redirect(url_for('login'))
