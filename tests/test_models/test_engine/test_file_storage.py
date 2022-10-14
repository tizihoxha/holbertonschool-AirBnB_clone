#!/usr/bin/python3
import models
from models import storage
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test__file_path(self):
        f = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(f))

    def test_save(self):
        """ Tests the save method for filestorage """
        my_obj = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
