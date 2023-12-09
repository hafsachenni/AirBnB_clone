#!/usr/bin/python3
"""
unittest for the amenity module
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    unittesting the amenity class
    """

    def test_name(self):
        amenity1 = Amenity()
        self.assertIsInstance(amenity1.name, str)


    def test_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)


    def test_str_repre(self):
        amenity = Amenity()
        expected = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(amenity.__str__(), expected)


    def test_is_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
