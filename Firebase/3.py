import os
import firebase_admin 
from firebase_admin import firestore
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
firebase_admin.initialize_app(cred)
db = firestore.client()

# CRUD Operations on DB                               --> Create, Read, Update, Delete

# Create                                              --> .add() or .set() command
C = {'name': 'Allen', 'age': 20}
db.collection('1').add(C)                             # Data added to a randomly generated ID in Collection 1
db.collection('2').document().set(C)                  # Data added to a randomly generated ID in Colection 2
db.collection('2').document('ID1').set(C)             # Data added to a user defined ID1 in Collection 2
db.collection('2').document('ID2').set(C)             # Data added to a user defined ID2 in Collection 2
C = {'age': 21, 'Address': ['Bangalore','Pune']}
db.collection('2').document('ID1').set(C, merge=True) # Data added to an existing document in Collection 2

# Read                                                --> .get() command
R = db.collection('2').document('ID').get()
if(R.exists): print(R.to_dict(),"\n")                 # Error Handling with .exists command
R = db.collection('2').get()
for r in R: print(r.to_dict())                        # Iterating through all documents in Collection 2
R = db.collection('2').where('age','==',21).get()     # Querying in Firestore with .where() command
for r in R: print("\nAge - 21: ",r.to_dict())                        
R = db.collection('2').where('Address','array_contains','Pune').get()
for r in R: print("\nLocation - Pune: ",r.to_dict())  # ('in', '['item1','item2']') for multiple queries

# Update                                              --> .update() command
U = {'age':22, 'Address': ['Bangalore','Kerala']}     # Data to be updated
db.collection('2').document('ID2').update(U)          # If data doesn't exist, it will be created
U = {'age':firestore.Increment(1)}                    # Incrementing age by 1
db.collection('2').document('ID2').update(U)  
U = {'Address': firestore.ArrayRemove('Kerala')}      # Removing Kerala from Address
db.collection('2').document('ID2').update(U)  
U = {'Address': firestore.ArrayUnion('Karnataka')}    # Adding Karnataka to Address
db.collection('2').document('ID2').update(U)      

# Delete                                              --> .delete() command
db.collection('2').document('ID2').update({'age':firestore.DELETE_FIELD})
db.collection('2').document('ID1').delete()           # Deleting documents with known ID
D = db.collection('1').get()                          # Deleting documents with unknown IDs
for d in D: db.collection('1').document(d.id).delete() 
D = db.collection('2').where('age','==',20).get()     # Deleting documents on condition
for d in D: db.collection('2').document(d.id).delete() 
db.collection('2').document('ID2').delete()           # Deleting documents with known ID

'''                                                   --> Cloud Firestore rules in Firebase
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
'''