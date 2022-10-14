#!/usr/bin/python3
"""Test file for User Class"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestUserClass(unittest.TestCase):
    """Test class for user"""
    def test_state(self):
        state1 = State()
        self.assertTrue(isinstance(state1, BaseModel))
