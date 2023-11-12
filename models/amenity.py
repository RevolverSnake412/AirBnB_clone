#!/usr/bin/python3
"""
Defining an Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    User class with one attribute
    (amenity name).
    """
    name = ""
