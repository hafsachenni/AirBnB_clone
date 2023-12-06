#!/usr/bin/python3

import json
from models.base_model import BaseModel

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
                    for key, obj_data in loaded_objects.items():
                        self.__objects[key] = eval(obj["__class__"])(**obj)
            except FileNotFoundError:
                pass


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
