#!/usr/bin/python3
"""
Defining a Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    User class with eleven attributes
    (city id, name id, name, description
    number of rooms and bathrooms, max guests
    price by night, latitude, longitude
    amenity ids).
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
