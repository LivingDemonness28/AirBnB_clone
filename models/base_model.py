#!/usr/bin/python3
"""Defines a BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents a Base model."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance with uuid and timestamps.

        Args:
            *args (any): Not used.
            **kwargs (dict): K/v pairs of attr.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        length = len(kwargs)
        time_type = "%Y-%m-%dT%H:%M:%S.%f"

        if length != 0:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(val, time_type)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Returns a dict representation of the BaseModel instance."""
        _dt = "%Y-%m-%dT%H:%M:%S.%f"
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = self.__class__.__name__
        res_dict['created_at'] = self.created_at.strftime(_dt)
        res_dict['updated_at'] = self.updated_at.strftime(_dt)
        return res_dict

    def save(self):
        """Updates the updated_at with current dt."""
        self.updated_at = datetime.now()
        models.storage.save()
