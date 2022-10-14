#!/usr/bin/python3
"""Test file for Amenity Class"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenityClass(unittest.TestCase):
    """Test class for user"""
    def test_state(self):
        am = Amenity()
        self.assertTrue(isinstance(am, BaseModel))

    def test_amenity_name(self):
        am = Amenity()
        self.assertEqual(str, type(am.name))
