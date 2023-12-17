#!/usr/bin/python3
"""Defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenity

    Attributes:
        name (str): Amenity name.
    """
    name = ""
