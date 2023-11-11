#!/usr/bin/python3
"""
Defining a User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class with four attributes
    (email, password, full name).
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
