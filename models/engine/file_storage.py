#!/usr/bin/python3
"""Module that holds Class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all dictionary"""
        return self.__objects

    def new(self, obj):
        """
        sets an object with a key.

        Args:
            obj: object to write
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialization"""
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserialization."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
