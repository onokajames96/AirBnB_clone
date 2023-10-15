#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """The base class."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance with a unique identifier.
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key != '__ class__':
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = class_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
