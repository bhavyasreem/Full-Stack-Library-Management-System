from pymongo import MongoClient

client = MongoClient(
    "........."
)

db = client["library"]

books = db["books"]
