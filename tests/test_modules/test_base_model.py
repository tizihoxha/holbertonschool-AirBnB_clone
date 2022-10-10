#!/usr/bin/python3
"""Test cases"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for base model"""
    def test__str(self):
        self.basemodel = BaseModel()
        output = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertEqual(print(self.basemodel), print(output))

        

