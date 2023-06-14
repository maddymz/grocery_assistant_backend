from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('./firebase-private.json')
default_app = initialize_app(cred)
db = firestore.client()
itemService = db.collection('items')
orderService = db.collection('orders')
userService = db.collection('users')
gptServiceDb = db.collection('chats')