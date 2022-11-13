from firebase_admin import credentials, firestore, initialize_app
from . import FIRESTORE_CREDENTIALS

# Initialize Firestore DB
print('Initializing Firestore DB...')
cred = credentials.Certificate(eval(FIRESTORE_CREDENTIALS))
default_app = initialize_app(cred)
db = firestore.client()