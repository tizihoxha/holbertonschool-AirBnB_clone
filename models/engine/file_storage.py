#!/usr/bin/python3
"""Task 5"""
import json
from models.base_model import BaseModel


class FileStorage:
    """File storage class created"""
    __file_path = "file.json"
    __objects = {}
    """class attributes"""

    def all(self):
        """Returns the dict objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in dict objects the obj with key clsname.id"""
        FileStorage.__objects[F"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes dict objects to the JSON file"""
        objDict = {}
        for key, value in FileStorage.__objects.items():
            objDict[key] = value.to_json()
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json.dumps(objDict))
