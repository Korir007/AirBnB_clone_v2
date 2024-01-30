#!/usr/bin/python3
""" """
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from os import getenv


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "Testing DBStorage only")
class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage class"""

    def setUp(self):
        """Set up the test environment"""
        self.db_storage = DBStorage()
        self.db_storage.reload()

    def tearDown(self):
        """Clean up after each test"""
        self.db_storage._DBStorage__session.close()
        self.db_storage._DBStorage__engine.dispose()

    def test_all_method(self):
        """Test the all method of DBStorage"""
        # Add test cases for the all method

    def test_new_method(self):
        """Test the new method of DBStorage"""
        # Add test cases for the new method

    def test_save_method(self):
        """Test the save method of DBStorage"""
        # Add test cases for the save method

    def test_delete_method(self):
        """Test the delete method of DBStorage"""
        # Add test cases for the delete method

    def test_reload_method(self):
        """Test the reload method of DBStorage"""
        # Add test cases for the reload method


if __name__ == '__main__':
    unittest.main()
