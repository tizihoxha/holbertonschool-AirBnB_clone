#!/usr/bin/python3
"""Unittest state"""
from models.state import State
from models.base_model import BaseModel
import unittest

class TestStateClass(unittest.TestCase):
    """unitest module testing for state class"""
    def test_state(self):
        s = State()
        self.assertTrue(isinstance(s, BaseModel))
