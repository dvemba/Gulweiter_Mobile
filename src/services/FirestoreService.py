import firebase_admin
from firebase_admin import credentials, firestore


import pyrebase


class FirestoreService:
    def __init__(self):
        cred = credentials.Certificate("src/services/serviceAccountKey.json")
        firebase_admin.initialize_app(cred) 
        self.db = firestore.client()
        
        pass
    def query_collection(self, collection_name, field, operator, value):
        print("Buscando dados do Firestore.")
        try:
            collection_ref = self.db.collection(collection_name)
            query = collection_ref.where(field, operator, value)
            results = [{"id": doc.id, "data": doc.to_dict()} for doc in query.stream()]
            return results
        except Exception as e:
            print(f"Erro ao realizar consulta: {e}")
            return None
    def get_document(self, collection_name, document_id):
        try:
            collection_ref = self.db.collection(collection_name)
            doc = collection_ref.document(document_id).get()
            if (doc.exists):
                return {**doc.to_dict(), 'id':doc.id}
        except:
            return None