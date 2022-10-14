#!/usr/bin/python3
"""Test file for City Class"""
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCityClass(unittest.TestCase):
    """Test class for city"""
    def test_city(self):
        city1 = City()
        self.assertTrue(isinstance(city1, BaseModel))

    def test_city_name(self):
        city1 = City()
        self.assertEqual(str, type(city1.name))
        self.assertEqual(str, type(city1.state_id))
