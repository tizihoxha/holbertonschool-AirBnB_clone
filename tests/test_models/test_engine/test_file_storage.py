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
