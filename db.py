import os
import pymongo


def connect_db():
    MONGODB_HOST = os.environ.get('MONGODB_HOST', 'localhost')
    MONGODB_PORT = os.environ.get('MONGODB_PORT', 27017)
    MONGODB_DB = os.environ.get('MONGODB_DB', 'podcast')

    mongo_client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = mongo_client[MONGODB_DB]

    return db
