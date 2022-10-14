#!/usr/bin/python3
import models
import os
import unittest
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test__file_path(self):
        f = FileStorage()
        self.assertTrue(hasattr(f, self.file_path))

    def test_save(self):
        """ Tests the save method for filestorage """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict1 = my_obj.all()
        my_obj.save()
        my_obj.reload()
        my_dict2 = my_obj.all()
        for key in my_dict1:
            key1 = key
        for key in my_dict2:
            key2 = key
        self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())

