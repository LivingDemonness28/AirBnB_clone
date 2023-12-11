#!/usr/bin/python3
"""Defines a BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents a Base model."""

    def __init__(self):
        """Initialize a BaseModel instance with uuid and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def to_dict(self):
        """Returns a dict representation of the BaseModel instance."""
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = self.__class__.__name__
        res_dict['created_at'] = self.created_at.isoformat()
        res_dict['updated_at'] = self.updated_at.isoformat()
        return res_dict

    def save(self):
        """
        Updates the updated_at with current dt.
        """
        self.updated_at = datetime.now()
