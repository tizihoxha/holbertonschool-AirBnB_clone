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

    def test_reload(self):
        b = BaseModel()
        models.storage.new(b)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b.id, obj)
   
    def test_save(self):
        b = BaseModel()
        models.storage.new(b)
        models.storage.save()
        text = ""
        with open("file.json") as f:
            text = f.read()
            self.assertIn("BaseModel." + b.id, text)
