#!/usr/bin/python3
"""unittests for cityity.py

unnitest classes:
    TestCitySave
    TestCityToDict
    TestCityInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.city import City


class TestCitySave(unittest.TestCase):
    """unittest: testing save method of City class"""
    
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
    
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_one(self):
        city = City()
        sleep(0.05)
        updt_at_1 = city.updated_at
        city.save()
        self.assertLess(updt_at_1, city.updated_at)

    def test_two(self):
        city = City()
        sleep(0.05)
        updt_at_1 = city.updated_at
        city.save()
        updt_at_2 = city.updated_at
        self.assertLess(updt_at_1, updt_at_2)
        sleep(0.05)
        city.save()
        self.assertLess(updt_at_2, city.updated_at)

    def test_updt_files(self):
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as file:
            self.assertIn(city_id, file.read())

class TestCityToDict(unittest.TestCase):
    """unittest: testing to_dict method of City class"""

    def test_output(self):
        _dt = datetime.now()
        city = City()
        city.id = "987654"
        city.created_at = city.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'City',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), t_dict)

    def test_type(self):
        city_type = type(City().to_dict())
        self.assertTrue(dict, city_type)

    def test_added_attr(self):
        city = City()
        city.second_name = "ALX"
        city.num = 28
        city_dict = city.to_dict()
        self.assertEqual("ALX", city.second_name)
        self.assertIn("num", city_dict)

    def test_correct_keys(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)

    def test_dt_attr_strs(self):
        city = City()
        city_dict = city.to_dict()
        self.assertTrue(isinstance(city_dict["id"], str))
        self.assertTrue(isinstance(city_dict["created_at"], str))
        self.assertTrue(isinstance(city_dict["updated_at"], str))

    def test_dunder_dict(self):
        city = City()
        city_dict = city.to_dict()
        city_dd = city.__dict__
        self.assertNotEqual(city_dict, city_dd)

    def test_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)

class TestCityInstantiation(unittest.TestCase):
    """unittest: testing instantiation of City class."""

    def test_id_pub_strs(self):
        city_id = City().id
        self.assertEqual(str, type(city_id))

    def test_created_at_pub_dt(self):
        city_ct = City().created_at
        self.assertEqual(datetime, type(city_ct))

    def test_updt_at_pub_dt(self):
        city_ut = City().updated_at
        self.assertEqual(datetime, type(city_ut))

    def test_2_city_uni_ids(self):
        city1_id = City().id
        city2_id = City().id
        self.assertNotEqual(city1_id, city2_id)

    def test_no_args_instantiate(self):
        city = City()
        self.assertEqual(City, type(city))

    def test_name_pub_cls_attr(self):
        city = City()
        city_name = City.name
        self.assertEqual(str, type(city_name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_state_id_pub_cls_attr(self):
        city = City()
        city_state_id = City.state_id
        self.assertEqual(str, type(city_state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_stored_in_obj(self):
        self.assertIn(City(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        city = City()
        city.id = "987654"
        city.created_at = city.updated_at = _dt
        city_str = city.__str__()
        self.assertIn("[City] (987654)", city_str)
        self.assertIn("'id': '987654'", city_str)
        self.assertIn("'created_at': " + _dt_rep, city_str)
        self.assertIn("'updated_at': " + _dt_rep, city_str)

    def test_2_diff_created_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.created_at, city_2.created_at)

    def test_2_diff_updt_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.updated_at, city_2.updated_at)

    def test_unused_args(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            City(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        city = City(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(city.id, "456")
        self.assertEqual(city.created_at, _dt)
        self.assertEqual(city.updated_at, _dt)


if __name__ == "__main__":
    unittest.main()