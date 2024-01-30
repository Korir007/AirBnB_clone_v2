#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up for each test"""
        pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test instantiation of BaseModel"""
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)

    def test_kwargs_initialization(self):
        """Test instantiation of BaseModel with kwargs"""
        instance = BaseModel()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertNotEqual(new_instance, instance)

    def test_save_method(self):
        """Test save method of BaseModel"""
        instance = BaseModel()
        instance.save()
        key = 'BaseModel.' + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_string_representation(self):
        """Test string representation of BaseModel"""
        instance = BaseModel()
        expected_str = '[BaseModel] ({}) {}'.format(instance.id,
                                                     instance.__dict__)
        self.assertEqual(str(instance), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel"""
        instance = BaseModel()
        dictionary = instance.to_dict()
        self.assertEqual(dictionary, instance.__dict__)

    def test_updated_at_after_save(self):
        """Test updated_at attribute after calling save method"""
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)


if __name__ == '__main__':
    unittest.main()
