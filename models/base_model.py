#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = None
        self.updated_at = None

        def __str__(self):
            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

        def save(self):
            self.updated_at = datetime.now()

        def to_dict(self):
            obj = self.__dict__.copy()
            obj['__class__'] = self.__class__.name__
            obj['created_at'] = self.created_at.isoformat()
            obj['updated_at'] = self.updated_at.isoformat()
            return obj


