#!/usr/bin/python3
"""Defines User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents user.

    Attributes:
        password (str): user password.
        email (str): user email.
        first_name (str): user first name.
        last_name (str): user last name.
    """

    password = ""
    email = ""
    first_name = ""
    last_name = ""
