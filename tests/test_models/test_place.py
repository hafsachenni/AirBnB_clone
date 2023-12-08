#!/usr/bin/python3
"""
unittest for the Place module
"""

import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """
    unittest for the place class
    """
    def test_instances_type(self):
        place1 = Place()
        self.assertIs(place1, type(Place))
        self.assertIsInstance(place1.id, str)
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)
    
    def test_rev_str_repr(self):
        place = Place()
        str_format = "[Review] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(place.__str__(), str_format)

    def _place_ids(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_place_save(self):
        place_3 = Place()
        updated_before_save = place_3.updated_at
        place_3.save()
        updated_after_save = place_3.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)

    def test_place_to_dict(self):
        place = Place()

        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())