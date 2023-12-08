#!/usr/bin/python3

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        obj = BaseModel()
        self.assertIsI
