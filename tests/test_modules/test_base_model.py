#!/usr/bin/python3
"""Test cases"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for base model"""
    def test__str__(self):
        self.basemodel = BaseModel()
        output = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertEqual(print(self.basemodel), print(output))

    def test_save(self):
        self.basemodel = BaseModel()
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))


        

