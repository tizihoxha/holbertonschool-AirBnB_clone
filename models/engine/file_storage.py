#!/usr/bin/python3
"""Task 5"""
import json
from models import BaseModel


class FileStorage:
    """File storage class created"""
    __file_path = "file.json"
    __objects = {}
    """class attributes"""

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[F"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        pass


