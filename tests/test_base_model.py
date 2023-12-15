#!/usr/bin/python3
"""Defines unnitest for base_models.py

Unittest classes:
    BaseModel_instantiation
    BaseModel_save
    BaseModel_to_dict
"""


import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel

class BaseModel_save(unittest.TestCase):
    """Unittests for save() in BaseModel class"""

    def test_save(self):
        my_mod = BaseModel()
        init_time = datetime.now()
        sim_time_passed = timedelta(seconds=1)
        nt = init_time + sim_time_passed
        my_mod.created_at = init_time
        my_mod.save()

class BaseModel_to_dict(unittest.TestCase):
    """Unittests for to_dict() in BaseModel class"""
    
    def test_to_dict(self):
        my_mod = BaseModel()
        mod_dict = my_mod.to_dict()
