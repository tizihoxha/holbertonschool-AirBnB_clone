#!/usr/bin/python3
"""Test file for Review Class"""
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReviewClass(unittest.TestCase):
    """Test class for review"""
    def test_review(self):
        rev = Review()
        self.assertTrue(isinstance(rev, BaseModel))

    def test_review_attr(self):
        rev = Review()
        self.assertEqual(str, type(rev.place_id))
        self.assertEqual(str, type(rev.user_id))
        self.assertEqual(str, type(rev.text))
