#!/usr/bin/python3
"""Defines unnitest for base_models.py

Unittest classes:
    BaseModel_to_dict
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel

class BaseModel_to_dict(unittest.TestCase):
    """Unittests for to_dict() in BaseModel class"""

    def test_output(self):
        my_mod = BaseModel()
        my_mod.id = "987654"
        dt = datetime.today()
        my_mod.created_at = my_mod.updated_at = dt
        mod_dict = my_mod.to_dict()
        td = {
            'id': '987654',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(mod_dict, td)
    
    def test_correct_keys(self):
        my_mod = BaseModel()
        mod_dict = my_mod.to_dict()
        self.assertIn("id", mod_dict)
        self.assertIn("created_at", mod_dict)
        self.assertIn("updated_at", mod_dict)
        self.assertIn("__class__", mod_dict)

    def test_to_dict(self):
        my_mod = BaseModel()
        mod_dict = my_mod.to_dict()
        self.assertTrue(dict, type(mod_dict))

    def test_attributes(self):
        my_mod = BaseModel()
        my_mod.name = "ALX"
        my_mod.num = 28
        mod_dict = my_mod.to_dict()
        self.assertIn("name", mod_dict)
        self.assertIn("num", mod_dict)

    def test_dict_dt_str(self):
        my_mod = BaseModel()
        mod_dict = my_mod.to_dict()
        self.assertEqual(str, type(mod_dict["created_at"]))
        self.assertEqual(str, type(mod_dict["updated_at"]))
    
    def test_dunder_dict(self):
        my_mod = BaseModel()
        mod_dict = my_mod.to_dict()
        self.assertNotEqual(mod_dict, my_mod.__dict__)

    def test_arg(self):
        my_mod = BaseModel()
        with self.assertRaises(TypeError):
            my_mod.to_dict(None)

    if __name__ == "__main__":
        unittest.main()
