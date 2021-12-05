import os
import firebase_admin 
from firebase_admin import db
from firebase_admin import credentials

# Loading variables from .env
from dotenv import load_dotenv
load_dotenv() 
p1=os.getenv('private_key_id')
p2=os.getenv('private_key')
p3=os.getenv('client_id')
u1=os.getenv('client_x509_cert_url')
u2=os.getenv('databaseURL')

# Creating credentials certificate for Authorization
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "learning-290101",
    "private_key_id": p1,
    "private_key": p2,
    "client_email": "firebase-adminsdk-x0tar@learning-290101.iam.gserviceaccount.com",
    "client_id": p3,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": u1
})

# Initializing the app with the certificate and access URL
firebase_admin.initialize_app(cred, {'databaseURL': u2})

# CRUD Operations on DB                             --> Create, Read, Update, Delete

# Create                                            --> .set() or .push() command
root = db.reference('')                             # Set Reference to the root of the DB '/'
C = root.child('users')                             # Set Reference to '/users' to variable c
C.set({                                     
    'Allen': {
        'date_of_birth': 'September 26, 2000',
        'full_name': 'Allen Ben Philipose',
        'age': 21
    },
    'Christi': {
        'date_of_birth': 'January 29, 2001',
        'full_name': 'Christiana John',
        'age': 20
    },
    'Alvin': {
        'date_of_birth': 'January 16, 2004',
        'full_name': 'Alvin Ben George',
        'nick_name': 'Avin Boo',
        'age': 17
    }
})                                          

# Read                                              --> .get() command
R = root.child('users').child('Christi')            # Set Reference to '/users/Christi' to variable r
print(R.get())                                      # Read the key 'Christi'
print("\nAge increasing order: ")
R = root.child('users').order_by_child('age')       # Sorting based on age
for z in R.get(): print("-",z)                      # Print all the keys
print("\nAge 20 and above: ")
R = root.child('users').order_by_child('age')       # Conditions based on age
for z in R.start_at(20).get(): print("-",z)         # Print all the keys

# Update                                            --> .update() command
U = root.child('users').child('Christi')            # Set Reference to '/users/Christi' to variable u
U.update({'nick_name': 'Kishti Mol'})               # Add new value with the key 'nick_name'
U = root.child('users').child('Alvin')              # Set Reference to '/users/Alvin' to variable u
U.update({'nick_name': 'Alvin Boo'})                # Update existing value of the key 'nick_name'

# Delete                                            --> .delete() or .remove() command
D = root.child('users').child('Allen')              # Set Reference to '/users/Allen' to variable d
D.delete()                                          # Delete the key 'Allen'

'''                                                 --> Realtime DB rules in Firebase
{
  "rules": {
    ".read": false,
    ".write": false,
    "users": {
      ".indexOn": ["full_name","nick_name","age"]
    }
  }
}
'''