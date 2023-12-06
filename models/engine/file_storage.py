#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage(BaseModel):

    __file_path = "file.json"
    __objects = {}
    
    
    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj


    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        data_to_save = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path, 'w') as f:
            json.dump(data_to_save, f)


    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        """

        with open(self.__file_path, 'r') as f:
            data_loaded = json.load(f)
        
            for key, obj_data in data_loaded.items():
                self.__objects[key] = eval(obj["__class__"])(**obj)

        

# obj = FileStorage()

# print(obj._FileStorage__file_path)
