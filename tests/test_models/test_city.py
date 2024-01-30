#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """Test cases for City class"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_type(self):
        """Test the type of state_id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.state_id), str)

    def test_name_type(self):
        """Test the type of name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)


if __name__ == '__main__':
    unittest.main()
