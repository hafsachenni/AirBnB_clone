#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:

        __file_path = "file.json"
        __objects = {}

        def all(self):
            return self.__objects

        def new(self, obj):
            self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

        def save(self):
            objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            with open(self.__file_path, "w", encoding='utf-8') as file: 
                json.dump(objects, file)


        def reload(self):
            try:
                with open(self.__file_path, "r", encoding='utf-8') as file:
                    loaded_objects = json.load(file)
                    for key, obj in loaded_objects.items():
                        self.__objects[key] = eval(obj["__class__"])(**obj)
            except FileNotFoundError:
                pass
