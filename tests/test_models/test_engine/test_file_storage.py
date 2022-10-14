#!/usr/bin/python3
"""unittesting file_storage"""
import models
from models import storage
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test filestorage"""
    def test__file_path(self):
        f = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(f))

    def test__objects(self):
        obj = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(obj))

    def test_all(self):
        obj = FileStorage()
        new_dict = obj.all()
        self.assertTrue(type(new_dict), dict)

    def test_new(self):
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        new_dict = obj.all()
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertTrue(key in new_dict)

    def test_save(self):
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        new_dict = obj.all()
        obj.save()
        obj.reload()
        dict2 = obj.all()
        for key in new_dict:
            key1 = key
        for key in dict2:
            key2 = key
        self.assertEqual(new_dict[key1].to_dict(), dict2[key2].to_dict())

    def test_reload(self):
        with open("test.json", "w") as f:
            obj = FileStorage()
            new_obj = BaseModel()
            obj.new(new_obj)
            obj.save()
            dict1 = obj.all()
        os.remove("test.json")
        obj.reload()
        dict2 = obj.all()
        self.assertEqual(dict1, dict2)
