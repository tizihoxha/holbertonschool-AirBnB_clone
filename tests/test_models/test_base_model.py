#!/usr/bin/python3
"""Test cases"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test class for base model"""
    def test_str_method(self):
        b = BaseModel()
        output = "[" + b.__class__.__name__ + "] " + "(" + b.id + ") " + str(b.__dict__)
        self.assertEqual(b.__str__(), output)

    def test_args_zero(self):
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_kwargs(self):
        date = datetime.now()
        dateiso = date.isoformat()
        b = BaseModel(id="123", created_at=dateiso, updated_at=dateiso)
        self.assertEqual(b.id, "123")
        self.assertEqual(b.created_at, date)
        self.assertEqual(b.updated_at, date)

    def test_save(self):
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

    def test_to_dict(self):
        b = BaseModel()
        bDict = b.to_dict()
        self.assertTrue(type(bDict["created_at"] == str))
