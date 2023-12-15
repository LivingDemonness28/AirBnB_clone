#!/usr/bin/python3
"""Defines a BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents a Base model."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance with uuid and timestamps."""
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dict representation of the BaseModel instance."""
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = self.__class__.__name__
        res_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        res_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return res_dict

    def save(self):
        """Updates the updated_at with current dt."""
        self.updated_at = datetime.now()
