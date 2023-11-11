#!/usr/bin/python3
"""
Defining a City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    User class with two attributes
    (state id, name of the state).
    """
    state_id = ""
    name = ""
