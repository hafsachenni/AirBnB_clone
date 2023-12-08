#!/usr/bin/python3
"""
unittest for the city module
"""

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel

class Testcity(unittest.TestCase):
    """
    unittest for the city class
    """

    def test_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_str_representation(self):
        city = City()
        expected = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(city.__str__(), expected)


    def test_instance(self):
        city = City()
        self.assertIs(type(city), City)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.id, str)
