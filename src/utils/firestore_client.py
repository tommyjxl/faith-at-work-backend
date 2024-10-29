import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirestoreClient():
	def __init__(self):
		# Initialize the app with a service account, granting admin privileges
		cred = credentials.Certificate('/mnt/c/Users/tommy/.ssh/firestore.json')
		firebase_admin.initialize_app(cred)

		# Create a Firestore client
		db = firestore.client()

	def demo_get(self):
		# Specify the collection name you want to fetch documents from
		collection_name = 'test-collection'

		# Fetch all documents in the specified collection
		docs = self.db.collection(collection_name).stream()

		# Print out each document's ID and data
		for doc in docs:
		    print(f'{doc.id} => {doc.to_dict()}')

