#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Test cases for State class"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test the type of name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)

    def test_cities_relationship(self):
        """Test the relationship with City class"""
        new_state = self.value()
        new_city = City(state_id=new_state.id)
        self.assertIn(new_city, new_state.cities)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
