# auth_functions.py
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    cred = credentials.Certificate("C:\\Users\\vigna\\Downloads\\domx-fab13-firebase-adminsdk-4qb8q-8ecda57187.json")  # Update path as necessary
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def sign_in(email, password):
    try:
        # Query Firestore for the user document with the provided email
        user_ref = db.collection('users').where('email', '==', email).limit(1).get()
        
        if not user_ref:
            return False, "No user record found for the provided email."
        
        user_doc = user_ref[0].to_dict()
        
        # Check if the password matches
        if user_doc.get('password') == password:
            return True, "Successfully signed in."
        else:
            return False, "Incorrect password."
    except Exception as e:
        return False, f"Error signing in: {e}"

def create_account(email, password):
    try:
        # Check if the email already exists
        existing_user_ref = db.collection('users').where('email', '==', email).limit(1).get()
        
        if existing_user_ref:
            return False, "User already exists with this email."

        # Create a new user document in Firestore
        db.collection('users').add({
            'email': email,
            'password': password  # Consider hashing passwords in production!
        })
        return True, "Successfully registered user."
    except Exception as e:
        return False, f"Error creating account: {e}"

def reset_password(email):
    try:
        # Logic for resetting password (you can implement this according to your requirements)
        return True, f"Reset password email sent to {email}"  # Placeholder for actual implementation
    except Exception as e:
        return False, f"Error sending reset password email: {e}"
