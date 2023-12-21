#!/usr/bin/python3
"""unittests for amenity.py

unnitest classes:
    TestAmenitySave
    TestAmenityToDict
    TestAmenityInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.amenity import Amenity


class TestAmenitySave(unittest.TestCase):
    """unittest: testing save method Amenity class"""

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

    def test_update_file(self):
        amen = Amenity()
        amen.save()
        amid = "Amenity." + amen.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_with_arg(self):
        amen = Amenity()
        with self.assertRaises(TypeError):
            amen.save(None)

    def test_one(self):
        amen = Amenity()
        sleep(0.05)
        updated_at_1 = amen.updated_at
        amen.save()
        self.assertLess(updated_at_1, amen.updated_at)

    def test_two(self):
        amen = Amenity()
        sleep(0.05)
        update_at_1 = amen.updated_at
        amen.save()
        update_at_2 = amen.updated_at
        self.assertLess(update_at_1, update_at_2)
        sleep(0.05)
        amen.save()
        self.assertLess(update_at_2, amen.updated_at)

class TestAmenityToDict(unittest.TestCase):
    """unittest: testing to_dict method Amenity class"""

    def test_output(self):
        _dt = datetime.now()
        amen = Amenity()
        amen.id = "987654"
        amen.created_at = amen.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'Amenity',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(amen.to_dict(), t_dict)

    def test_save(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_type(self):
        amen_type = type(Amenity().to_dict())
        self.assertTrue(dict, amen_type)

    def test_added_attr(self):
        amen = Amenity()
        amen.second_name = "ALX"
        amen.num = 28
        self.assertEqual("ALX", amen.second_name)
        self.assertIn("num", amen.to_dict)

    def test_correct_keys(self):
        amen = Amenity()
        amen_dict = amen.to_dict()
        self.assertIn("id", amen_dict)
        self.assertIn("created_at", amen_dict)
        self.assertIn("updated_at", amen_dict)
        self.assertIn("__class__", amen_dict)

    def test_dt_attr_strs(self):
        amen = Amenity()
        amen_dict = amen.to_dict()
        self.assertTrue(isinstance(amen_dict["id"], str))
        self.assertTrue(isinstance(amen_dict["created_at"], str))
        self.assertTrue(isinstance(amen_dict["updated_at"], str))

    def test_arg(self):
        amen = Amenity()
        with self.assertRaises(TypeError):
            amen.to_dict(None)

    def test_dunder_dict(self):
        amen = Amenity()
        amen_dict = amen.to_dict()
        amen_dd = amen.__dict__
        self.assertNotEqual(amen_dict, amen_dd)

class TestAmenityInstantiation(unittest.TestCase):
    """unittest: testing instantiation of Amenity class."""

    def test_id_pub_strs(self):
        amen_id = Amenity().id
        self.assertEqual(str, type(amen_id))

    def test_created_at_pub_dt(self):
        amen_ct = Amenity().created_at
        self.assertEqual(datetime, type(amen_ct))

    def test_updated_at_pub_dt(self):
        amen_ut = Amenity().updated_at
        self.assertEqual(datetime, type(amen_ut))

    def test_2_amen_uni_ids(self):
        amen1_id = Amenity().id
        amen2_id = Amenity().id
        self.assertNotEqual(amen1_id, amen2_id)

    def test_no_args_instantiate(self):
        amen = Amenity()
        self.assertEqual(Amenity, type(amen))

    def test_name_pub_cls_attr(self):
        amen = Amenity()
        amen_name = Amenity.name
        self.assertEqual(str, type(amen_name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen.__dict__)

    def test_stored_in_obj(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        amen = Amenity()
        amen.id = "987654"
        amen.created_at = amen.updated_at = _dt
        amen_str = amen.__str__()
        self.assertIn("[Amenity] (987654)", amen_str)
        self.assertIn("'id': '987654'", amen_str)
        self.assertIn("'created_at': " + _dt_rep, amen_str)
        self.assertIn("'updated_at': " + _dt_rep, amen_str)

    def test_2_diff_created_at(self):
        amen_1 = Amenity()
        sleep(0.05)
        amen_2 = Amenity()
        self.assertLess(amen_1.created_at, amen_2.created_at)

    def test_2_diff_updt_at(self):
        amen_1 = Amenity()
        sleep(0.05)
        amen_2 = Amenity()
        self.assertLess(amen_1.updated_at, amen_2.updated_at)

    def test_created_at_is_pub_dt(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updt_at_is_pub_dt(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_unused_args(self):
        amen = Amenity(None)
        self.assertNotIn(None, amen.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        amen = Amenity(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(amen.id, "456")
        self.assertEqual(amen.created_at, _dt)
        self.assertEqual(amen.updated_at, _dt)

if __name__ == "__main__":
    unittest.main()
