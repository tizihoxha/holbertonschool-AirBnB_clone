#!/usr/bin/python3
"""Test file for User Class"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUserClass(unittest.TestCase):
    """Test class for user"""
    def test_user(self):
        user1 = User()
        self.assertTrue(isinstance(user1, BaseModel))

    def test_user_email(self):
        user1 = User()
        self.assertEqual(str, type(user1.email))

    def test_user_password(self):
        user1 = User()
        self.assertEqual(str, type(user1.password))

    def test_user_first_name(self):
        user1 = User()
        self.assertEqual(str, type(user1.first_name))

    def test_user_last_name(self):
        user1 = User()
        self.assertEqual(str, type(user1.last_name))
