#!/usr/bin/python3
"""unittests for BaseModel.py

unnitest classes:
    TestBaseModelSave
    TestBaseModelToDict
    TestBaseModelInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.base_model import BaseModel

class TestBaseModelSave(unittest.TestCase):
    """unittest: testing save method BaseModel class"""

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
        base_mod = BaseModel()
        base_mod.save()
        amid = "BaseModel." + base_mod.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_with_arg(self):
        base_mod = BaseModel()
        with self.assertRaises(TypeError):
            base_mod.save(None)

    def test_one(self):
        base_mod = BaseModel()
        sleep(0.05)
        updated_at_1 = base_mod.updated_at
        base_mod.save()
        self.assertLess(updated_at_1, base_mod.updated_at)

    def test_two(self):
        base_mod = BaseModel()
        sleep(0.05)
        update_at_1 = base_mod.updated_at
        base_mod.save()
        update_at_2 = base_mod.updated_at
        self.assertLess(update_at_1, update_at_2)
        sleep(0.05)
        base_mod.save()
        self.assertLess(update_at_2, base_mod.updated_at)

class TestBaseModelToDict(unittest.TestCase):
    """unittest: testing to_dict method BaseModel class"""

    def test_output(self):
        _dt = datetime.now()
        base_mod = BaseModel()
        base_mod.id = "987654"
        base_mod.created_at = base_mod.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'BaseModel',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(base_mod.to_dict(), t_dict)

    def test_type(self):
        base_mod_type = type(BaseModel().to_dict())
        self.assertTrue(dict, base_mod_type)

    def test_added_attr(self):
        base_mod = BaseModel()
        base_mod.second_name = "ALX"
        base_mod.num = 28
        base_mod_dict = base_mod.to_dict()
        self.assertEqual("ALX", base_mod.second_name)
        self.assertIn("num", base_mod_dict)

    def test_correct_keys(self):
        base_mod = BaseModel()
        base_mod_dict = base_mod.to_dict()
        self.assertIn("id", base_mod_dict)
        self.assertIn("created_at", base_mod_dict)
        self.assertIn("updated_at", base_mod_dict)
        self.assertIn("__class__", base_mod_dict)

    def test_dt_attr_strs(self):
        base_mod = BaseModel()
        base_mod_dict = base_mod.to_dict()
        self.assertTrue(isinstance(base_mod_dict["id"], str))
        self.assertTrue(isinstance(base_mod_dict["created_at"], str))
        self.assertTrue(isinstance(base_mod_dict["updated_at"], str))

    def test_arg(self):
        base_mod = BaseModel()
        with self.assertRaises(TypeError):
            base_mod.to_dict(None)

    def test_dunder_dict(self):
        base_mod = BaseModel()
        base_mod_dict = base_mod.to_dict()
        base_mod_dd = base_mod.__dict__
        self.assertNotEqual(base_mod_dict, base_mod_dd)

class TestBaseModelInstantiation(unittest.TestCase):
    """unittest: testing instantiation of BaseModel class."""

    def test_id_pub_strs(self):
        base_mod_id = BaseModel().id
        self.assertEqual(str, type(base_mod_id))

    def test_created_at_pub_dt(self):
        base_mod_ct = BaseModel().created_at
        self.assertEqual(datetime, type(base_mod_ct))

    def test_updated_at_pub_dt(self):
        base_mod_ut = BaseModel().updated_at
        self.assertEqual(datetime, type(base_mod_ut))

    def test_2_base_mod_uni_ids(self):
        base_mod1_id = BaseModel().id
        base_mod2_id = BaseModel().id
        self.assertNotEqual(base_mod1_id, base_mod2_id)

    def test_no_args_instantiate(self):
        base_mod = BaseModel()
        self.assertEqual(BaseModel, type(base_mod))

    def test_stored_in_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        base_mod = BaseModel()
        base_mod.id = "987654"
        base_mod.created_at = base_mod.updated_at = _dt
        base_mod_str = base_mod.__str__()
        self.assertIn("[BaseModel] (987654)", base_mod_str)
        self.assertIn("'id': '987654'", base_mod_str)
        self.assertIn("'created_at': " + _dt_rep, base_mod_str)
        self.assertIn("'updated_at': " + _dt_rep, base_mod_str)

    def test_2_diff_created_at(self):
        base_mod_1 = BaseModel()
        sleep(0.05)
        base_mod_2 = BaseModel()
        self.assertLess(base_mod_1.created_at, base_mod_2.created_at)

    def test_2_diff_updt_at(self):
        base_mod_1 = BaseModel()
        sleep(0.05)
        base_mod_2 = BaseModel()
        self.assertLess(base_mod_1.updated_at, base_mod_2.updated_at)

    def test_unused_args(self):
        base_mod = BaseModel(None)
        self.assertNotIn(None, base_mod.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        base_mod = BaseModel(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(base_mod.id, "456")
        self.assertEqual(base_mod.created_at, _dt)
        self.assertEqual(base_mod.updated_at, _dt)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        base_mod = BaseModel("28", id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(base_mod.id, "456")
        self.assertEqual(base_mod.created_at, _dt)
        self.assertEqual(base_mod.updated_at, _dt)


if __name__ == "__main__":
        unittest.main()
