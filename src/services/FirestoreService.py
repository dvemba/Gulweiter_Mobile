import firebase_admin
from firebase_admin import credentials, firestore


import pyrebase


class FirestoreService:
    def __init__(self):
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred) 
        db = firestore.client()
        pass