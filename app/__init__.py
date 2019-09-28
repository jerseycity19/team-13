from firebase_admin import credentials, firestore, initialize_app, storage
from flask import Flask

app = Flask(__name__)

# Use the application default credentials
cred = credentials.Certificate('firebase.json')
initialize_app(cred, {
    'projectId': "code-for-good-nj-13",
    'storageBucket': 'code-for-good-nj-13.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

from app import routes
