#!/usr/bin/python3
"""Task 8"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class user that inherts from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
