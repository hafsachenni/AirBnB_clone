#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()
    
    def to_dict(self):
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        return self.__dict__


    def get_id(self):
        return self.id