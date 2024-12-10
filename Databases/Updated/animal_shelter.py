import logging
from pymongo import MongoClient, ASCENDING, errors
import urllib.parse
import pandas as pd
from cachetools import cached, TTLCache

class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username="farrik", password="SNHU1234"):
        """
        Initializes the MongoClient to access the MongoDB database and collections.
        
        Args:
            username (str): The username for the database connection.
            password (str): The password for the database connection.
        """
        self.USER = urllib.parse.quote_plus(username)
        self.PASS = urllib.parse.quote_plus(password)
        self.HOST = 'localhost'
        self.PORT = 27017
        self.DB = 'AAC'
        self.COL = 'animals'
        
        self.client = self.connect_to_db()
        self.database = self.client[self.DB]
        self.collection = self.database[self.COL]

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.remove_duplicates()
        self.optimize_indexes()
    
    def connect_to_db(self):
        return MongoClient(f'mongodb://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/?authSource=admin', maxPoolSize=50)

    def remove_duplicates(self):
        pipeline = [
            {"$group": {"_id": "$animal_id", "count": {"$sum": 1}, "ids": {"$push": "$_id"}}},
            {"$match": {"count": {"$gt": 1}}}
        ]
        duplicates = list(self.collection.aggregate(pipeline))
        for duplicate in duplicates:
            ids = duplicate["ids"]
            for doc_id in ids[1:]:
                self.collection.delete_one({"_id": doc_id})

    def optimize_indexes(self):
        self.collection.create_index([('animal_id', ASCENDING)], unique=True)
        self.collection.create_index([('name', ASCENDING)])
        self.collection.create_index([('species', ASCENDING)])

    def validate_data(self, data):
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        required_fields = ["animal_id", "name", "species"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        return True

    def create(self, data):
        """
        Create a new animal record in the collection.
        
        Args:
            data (dict): The data for the new animal record.
        
        Returns:
            ObjectId: The ID of the inserted document, or None if the insertion failed.
        
        Raises:
            TypeError: If the data is not a dictionary.
            ValueError: If the animal ID already exists or if data is empty.
            RuntimeError: If the record creation fails due to other reasons.
        """
        self.validate_data(data)
        try:
            existing_record = self.collection.find_one({"animal_id": data.get("animal_id")})
            if existing_record:
                raise ValueError("Animal with this ID already exists.")
                
            result = self.collection.insert_one(data)
            self.logger.info(f"Animal {data['animal_id']} created successfully")
            return result.inserted_id if result.acknowledged else None
        except errors.DuplicateKeyError:
            self.logger.error(f"Duplicate animal_id: {data.get('animal_id')}")
            raise ValueError(f"Animal with ID {data.get('animal_id')} already exists.")
        except Exception as e:
            self.logger.error("Failed to create animal record: " + str(e))
            raise RuntimeError("Failed to create animal record: " + str(e))

    def create_bulk(self, data_list):
        if not isinstance(data_list, list):
            raise TypeError("Data must be a list of dictionaries")
        try:
            result = self.collection.insert_many(data_list, ordered=False)
            self.logger.info(f"Inserted {len(result.inserted_ids)} animals")
            return result.inserted_ids if result.acknowledged else None
        except errors.BulkWriteError as e:
            self.logger.error("Bulk write error: " + str(e))
            raise RuntimeError("Bulk write error: " + str(e))

    cache = TTLCache(maxsize=100, ttl=300)

    @cached(cache, key=lambda self, readData=None, page=1, page_size=10, sort_by='animal_id': (
        frozenset(readData.items()) if readData else None, page, page_size, sort_by))
    def read(self, readData=None, page=1, page_size=10, sort_by='animal_id'):
        """
        Read from the collection with pagination and sorting.
        
        Args:
            readData (dict): The filter criteria for reading data.
            page (int): The page number for pagination.
            page_size (int): The number of records per page.
            sort_by (str): The field to sort the results by.
        
        Returns:
            list: A list of animal records matching the criteria.
        
        Raises:
            RuntimeError: If the read operation fails.
        """
        try:
            skip = (page - 1) * page_size
            cursor = self.collection.find(readData or {}, {"_id": False}).sort(sort_by, ASCENDING).skip(skip).limit(page_size)
            result = list(cursor)
            self.logger.info(f"Read {len(result)} animals")
            return result
        except Exception as e:
            self.logger.error("Failed to read animal records: " + str(e))
            raise RuntimeError("Failed to read animal records: " + str(e))

    def update(self, old_data, new_data):
        """
        Update an existing animal record in the collection.
        
        Args:
            old_data (dict): The filter criteria to find the existing record.
            new_data (dict): The new data to update the record with.
        
        Returns:
            bool: True if the record was updated, False otherwise.
        
        Raises:
            RuntimeError: If the update operation fails.
        """
        try:
            result = self.collection.update_one(old_data, {'$set': new_data})
            if result.modified_count:
                self.logger.info("Animal updated successfully")
                return True
            else:
                self.logger.warning("Animal not found")
                return False
        except Exception as e:
            self.logger.error("Failed to update animal record: " + str(e))
            raise RuntimeError("Failed to update animal record: " + str(e))

    def delete(self, deleteData):
        """
        Delete an animal record from the collection.
        
        Args:
            deleteData (dict): The filter criteria to find the record to delete.
        
        Returns:
            bool: True if the record was deleted, False otherwise.
        
        Raises:
            RuntimeError: If the delete operation fails.
        """
        try:
            result = self.collection.delete_one(deleteData)
            if result.deleted_count:
                self.logger.info("Animal deleted successfully")
                return True
            else:
                self.logger.warning("Animal not found")
                return False
        except Exception as e:
            self.logger.error("Failed to delete animal record: " + str(e))
            raise RuntimeError("Failed to delete animal record: " + str(e))

    def get_animal_stats(self):
        """
        Get aggregated statistics of animals by species.
        
        Returns:
            list: A list of aggregated statistics.
        
        Raises:
            RuntimeError: If the aggregation operation fails.
        """
        pipeline = [
            {"$group": {"_id": "$species", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        try:
            result = list(self.collection.aggregate(pipeline))
            self.logger.info(f"Aggregated stats: {result}")
            return result
        except Exception as e:
            self.logger.error("Failed to get animal stats: " + str(e))
            raise RuntimeError("Failed to get animal stats: " + str(e))

def load_data(db, filter_criteria={}):
    """
    Load animal data from the database and return it as a Pandas DataFrame.
    
    Args:
        db (AnimalShelter): The AnimalShelter instance.
        filter_criteria (dict): The filter criteria for reading data.
    
    Returns:
        DataFrame: A Pandas DataFrame containing the animal data.
    """
    try:
        df = pd.DataFrame.from_records(db.read(filter_criteria))
        if '_id' in df.columns:
            df.drop(columns=['_id'], inplace=True)
        return df
    except Exception as e:
        logging.getLogger(__name__).error(f"Error loading data: {e}")
        return pd.DataFrame()









