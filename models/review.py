#!/usr/bin/python3
"""
Defining a Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class with three attributes
    (IDs of place and user, text).
    """
    place_id = ""
    user_id = ""
    text = ""
