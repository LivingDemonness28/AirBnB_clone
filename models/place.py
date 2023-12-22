#!/usr/bin/python3
"""Define Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent place

    Args:
        city_id (str): City id.
        name (str): Place name.
        user_id (str): User id.
        description (str): Place description.
        number_rooms (int): Num of rooms.
        number_bathrooms (int): Num of bathrooms.
        max_guest (int): Max num of guests.
        price_by_night (int): Price by night.
        latitude (float): Place latitude.
        longitude (float): Place longitude.
        amenity_ids (list): Amenity ids list.
    """

    city_id = ""
    name = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
