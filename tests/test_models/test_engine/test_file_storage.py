#!/usr/bin/python3
"""
unittest for filestorage module
"""
import unittest
from models.engine.file_storage import FileStorage
import models
from models.user import User
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    testing the filestorage class
    """

    def test_instance(self):
        self.assertIs(FileStorage, type(FileStorage()))
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)


    def test_all_in_storage(self):
        self.assertEqual(type(models.storage.all()), dict) 


    def test_FileStorage(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
