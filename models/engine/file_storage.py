#!/usr/bin/python3
"""Task 5"""
import json
from os import path


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
            objDict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objDict, f)

    def reload(self):
        """Deserializes the JSON file to dict objects"""
        from models.base_model import BaseModel
        from models.user import User
        if path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                objDict = json.load(f)
            for key, value in objDict.items():
                self.__objects[key] = BaseModel(**value)
                # self.__objects[key] = User(**value)
