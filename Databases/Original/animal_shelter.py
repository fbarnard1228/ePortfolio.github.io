from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username="accfarrik", password="SNHU1234"):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacfarrik'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30349
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)
            print("Animal created successfully")
            return result.inserted_id if result.acknowledged else None
        else:
            raise ValueError("Nothing to save because data parameter is empty")
    
    def read(self, readData):
        if readData is not None:
            result = list(self.database.animals.find(readData))
        else:
            result = self.database.animals.find({}, {"_id": False})
            print("Animal read unsuccessfully")
        return result if result else []

    def update(self,old_data, new_data):
        result = self.database.animals.update_one(old_data, {'$set': new_data})
        if result.modified_count:
            print("Animal updated successfully")
        else:
            print("Animal not found")

    def delete(self,deleteData):
        result = self.database.animals.delete_one(deleteData)
        if result.deleted_count:
            print("Animal deleted successfully")
        else:
            print("Animal not found")