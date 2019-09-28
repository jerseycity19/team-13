from firebase_admin import credentials, firestore, initialize_app, storage
from flask import Flask
from os.path import abspath, dirname, join
from os import mkdir

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

try:
    mkdir(app.config['UPLOAD_FOLDER'])
except FileExistsError:
    pass

# Use the application default credentials
cred = credentials.Certificate('firebase.json')
initialize_app(cred, {
    'projectId': "code-for-good-nj-13",
    'storageBucket': 'code-for-good-nj-13.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

from app import routes
