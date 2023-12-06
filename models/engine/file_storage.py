#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:

    def __init__(self, file_path, objects):
        self.__file_path = file.json
        self.__objects = {}

    def all(self):
        return self.__objects

