#!/usr/bin/python3

import uuid
from datetime import datetime



class BaseModel:
    """The base class."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance with a unique identifier.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__ class__':
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
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

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

