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
        my_obj = BaseModel()
        Storage.save()
        self.assertTrues(os.path.exists("file.json"))
