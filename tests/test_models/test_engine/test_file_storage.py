#!/usr/bin/python3
import models
import unittest
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test__file_path(self):
        f = FileStorage()
        self.assertTrue(hasattr(self.f, __file_path))

