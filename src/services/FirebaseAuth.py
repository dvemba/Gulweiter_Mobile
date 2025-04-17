import pyrebase


class FirebaseAuth:
    def __init__(self):
        firebaseConfig = {
            "apiKey": "AIzaSyB4sOlcaXn7Y01QpERvtuPGmX-gF90SjIs",
            "authDomain": "foodiehub-22698.firebaseapp.com",
            "databaseURL": "https://foodiehub-22698-default-rtdb.europe-west1.firebasedatabase.app",
            "projectId": "foodiehub-22698",
            "storageBucket": "foodiehub-22698.firebasestorage.app",
            "messagingSenderId": "654144144680",
            "appId": "1:654144144680:web:a546210bb30891c8ab7c1d"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()
        pass
    
    def sign_in(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            # print(f"Login feito com sucesso: {user['email']}")
            # print(user)
            return [True, user]
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        