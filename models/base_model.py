#!/usr/bin/python3

import uuid
from datetime import datetime



class BaseModel:
    """The base class."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance with a unique identifier.
        """
