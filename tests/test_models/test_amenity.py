#!/usr/bin/python3

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(test_basemodel):
    """Test class for Amenity"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_create_instance_with_parameters(self):
        """Test creating an instance of Amenity with parameters"""
        params = {'name': 'New Amenity', 'param2': 42, 'param3': 3.14}
        new_instance = self.value(**params)

        self.assertEqual(new_instance.name, 'New Amenity')
        self.assertEqual(new_instance.param2, 42)
        self.assertEqual(new_instance.param3, 3.14)

        # Additional assertions or cleanup if needed

if __name__ == '__main__':
    unittest.main()
