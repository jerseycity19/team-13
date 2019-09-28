from firebase_admin import credentials, firestore, initialize_app
from flask import Flask

app = Flask(__name__)

# Use the application default credentials
cred = credentials.ApplicationDefault()
initialize_app(cred, {
  'projectId': "code-for-good-nj-13",
})

db = firestore.client()

from app import routes
