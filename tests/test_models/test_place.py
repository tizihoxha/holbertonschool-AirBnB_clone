#!/usr/bin/python3
"""Test file for Place Class"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceClass(unittest.TestCase):
    """Test class for place"""
    def test_place(self):
        plc = Place()
        self.assertTrue(isinstance(plc, BaseModel))

    def test_place_attr(self):
        plc = Place()
        self.assertEqual(str, type(plc.city_id))
        self.assertEqual(str, type(plc.user_id))
        self.assertEqual(str, type(plc.name))
        self.assertEqual(str, type(plc.description))
        self.assertEqual(int, type(plc.number_rooms))
        self.assertEqual(int, type(plc.number_bathrooms))
        self.assertEqual(int, type(plc.max_guest))
        self.assertEqual(int, type(plc.price_by_night))
        self.assertEqual(float, type(plc.latitude))
        self.assertEqual(float, type(plc.longitude))
        self.assertEqual(list, type(plc.amenity_ids))
