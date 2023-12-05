#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        def __str__(self):
            return "[{}] ({})












        def get_id(self):
            return self.id
