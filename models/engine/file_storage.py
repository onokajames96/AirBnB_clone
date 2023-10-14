#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return FileStora.__objects
    def save(self):
        with open("storage.json", "w") as file:
            json.dump(self.objects, file)
