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
                if key is not '__ class__':

