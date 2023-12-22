#!/usr/bin/python3
"""Defines unittests for file_storage.py

Unittest classes:
    Test_FS_Methods
    Test_FS_Instantion
"""
import unittest
import json
import os
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class Test_FS_Methods(unittest.TestCase):
    """unittest: testing methods of FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new(self):
        amen = Amenity()
        base_mod = BaseModel()
        city = City()
        place = Place()
        rev = Review()
        state = State()
        usr = User()
        models.storage.new(amen)
        models.storage.new(base_mod)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(rev)
        models.storage.new(state)
        models.storage.new(usr)
        key = models.storage.all().keys()
        val = models.storage.all().values()
        self.assertIn("Amenity." + amen.id, key)
        self.assertIn(amen, val)
        self.assertIn("BaseModel." + base_mod.id, key)
        self.assertIn(base_mod, val)
        self.assertIn("City." + city.id, key)
        self.assertIn(city, val)
        self.assertIn("Place." + place.id, key)
        self.assertIn(place, val)
        self.assertIn("Review." + place.id, key)
        self.assertIn(rev, val)
        self.assertIn("State." + state.id, key)
        self.assertIn(state, val)
        self.assertIn("User." + usr.id, key)
        self.assertIn(usr, val)

    def test_save(self):
        amen = Amenity()
        base_mod = BaseModel()
        city = City()
        place = Place()
        rev = Review()
        state = State()
        usr = User()
        models.storage.new(amen)
        models.storage.new(base_mod)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(rev)
        models.storage.new(state)
        models.storage.new(usr)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("Amenity." + amen.id, save_text)
            self.assertIn("BaseModel." + base_mod.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("Review." + rev.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("User." + usr.id, save_text)

    def test_reload(self):
        amen = Amenity()
        base_mod = BaseModel()
        city = City()
        place = Place()
        rev = Review()
        state = State()
        usr = User()
        models.storage.new(amen)
        models.storage.new(base_mod)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(rev)
        models.storage.new(state)
        models.storage.new(usr)
        models.storage.save()
        models.storage.reload()
        o = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + amen.id, o)
        self.assertIn("BaseModel." + base_mod.id, o)
        self.assertIn("City." + city.id, o)
        self.assertIn("Place." + place.id, o)
        self.assertIn("Review." + rev.id, o)
        self.assertIn("State." + state.id, o)
        self.assertIn("User." + usr.id, o)

    def test_all(self):
        All = models.storage.all()
        self.assertEqual(dict, type(All))

    def test_all_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_arg(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
