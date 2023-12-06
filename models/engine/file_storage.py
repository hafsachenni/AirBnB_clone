#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:

    def __init__(self, file_path, objects):
        self.__file_path = file.json
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        objects = {key: obj.to_dict() for key, obj in self.__objects__.items()
        with open (__file_path, "w", encoding='utf-8') as file: 
            json.dump(objects, file)


    def relaod(self):
        with open(__file__path, "r", encoding='utf-8') as file:
            json.load(objects, file)
