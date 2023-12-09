#!/usr/bin/python3
"""
unittest for the sate module
"""

import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """
    testing of state class
    that inherits from basemodel
    """
    def test_type_of_name(self):
        state = State()
        self.assertEqual(type(State.name), str)


    def test_ids(self):
        test1 = State()
        test2 = State()
        self.assertNotEqual(test1.id, test2.id)


    def test_str_representation(self):
        state = State()
        expected = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(state.__str__(), expected)
