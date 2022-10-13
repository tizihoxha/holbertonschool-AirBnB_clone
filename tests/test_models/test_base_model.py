#!/usr/bin/python3
"""Test cases"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for base model"""
    def test_str_method(self):
        b = BaseModel()
        output = "[" + b.__class__.__name__ + "] " + "(" + b.id + ") " + str(b.__dict__)
        self.assertEqual(b.__str__(), output)

    def test_save_method(self):
        b = BaseModel()
        old = b.updated_at
        b.save()
        new = b.updated_at
        self.assertTrue(new > old)

    def test_id(self):
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "id"))

    def test_created_at(self):
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
