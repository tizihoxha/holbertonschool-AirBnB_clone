#!/usr/bin/python3
"""unittesting file_storage"""
import models
import json
from models import storage
import unittest
import os
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
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
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        text = ""
        with open("file.json") as f:
            text = f.read()
            self.assertIn("BaseModel." + b.id, text)
            self.assertIn("User." + u.id, text)
            self.assertIn("State." + s.id, text)
            self.assertIn("Place." + p.id, text)
            self.assertIn("City." + c.id, text)
            self.assertIn("Amenity." + a.id, text)
            self.assertIn("Review." + r.id, text)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b.id, obj)
        self.assertIn("User." + u.id, obj)
        self.assertIn("State." + s.id, obj)
        self.assertIn("Place." + p.id, obj)
        self.assertIn("City." + c.id, obj)
        self.assertIn("Amenity." + a.id, obj)
        self.assertIn("Review." + r.id, obj)

    """
    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())
    """

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

if __name__ == "__main__":
    unittest.main()
