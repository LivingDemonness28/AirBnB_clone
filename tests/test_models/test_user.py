#!/usr/bin/python3
"""unittests for User.py

unnitest classes:
    TestUserSave
    TestUserToDict
    TestUserInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.user import User


class TestUserSave(unittest.TestCase):
    """unittest: testing save method User class"""

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
        usr = User()
        usr.save()
        amid = "User." + usr.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_one(self):
        usr = User()
        sleep(0.05)
        updated_at_1 = usr.updated_at
        usr.save()
        self.assertLess(updated_at_1, usr.updated_at)

    def test_two(self):
        usr = User()
        sleep(0.05)
        update_at_1 = usr.updated_at
        usr.save()
        update_at_2 = usr.updated_at
        self.assertLess(update_at_1, update_at_2)
        sleep(0.05)
        usr.save()
        self.assertLess(update_at_2, usr.updated_at)

class TestUserToDict(unittest.TestCase):
    """unittest: testing to_dict method User class"""

    def test_output(self):
        _dt = datetime.now()
        usr = User()
        usr.id = "987654"
        usr.created_at = usr.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'User',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), t_dict)

    def test_save(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_type(self):
        usr_type = type(User().to_dict())
        self.assertTrue(dict, usr_type)

    def test_added_attr(self):
        usr = User()
        usr.second_name = "ALX"
        usr.num = 28
        usr_dict = usr.to_dict()
        self.assertEqual("ALX", usr.second_name)
        self.assertIn("num", usr_dict)

    def test_correct_keys(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertIn("id", usr_dict)
        self.assertIn("created_at", usr_dict)
        self.assertIn("updated_at", usr_dict)
        self.assertIn("__class__", usr_dict)

    def test_dt_attr_strs(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertTrue(isinstance(usr_dict["id"], str))
        self.assertTrue(isinstance(usr_dict["created_at"], str))
        self.assertTrue(isinstance(usr_dict["updated_at"], str))

    def test_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)

    def test_dunder_dict(self):
        usr = User()
        usr_dict = usr.to_dict()
        usr_dd = usr.__dict__
        self.assertNotEqual(usr_dict, usr_dd)

class TestUserInstantiation(unittest.TestCase):
    """unittest: testing instantiation of User class."""

    def test_id_pub_strs(self):
        usr_id = User().id
        self.assertEqual(str, type(usr_id))

    def test_created_at_pub_dt(self):
        usr_ct = User().created_at
        self.assertEqual(datetime, type(usr_ct))

    def test_updated_at_pub_dt(self):
        usr_ut = User().updated_at
        self.assertEqual(datetime, type(usr_ut))

    def test_2_usr_uni_ids(self):
        usr1_id = User().id
        usr2_id = User().id
        self.assertNotEqual(usr1_id, usr2_id)

    def test_no_args_instantiate(self):
        usr = User()
        self.assertEqual(User, type(usr)) 

    def test_stored_in_obj(self):
        self.assertIn(User(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        usr = User()
        usr.id = "987654"
        usr.created_at = usr.updated_at = _dt
        usr_str = usr.__str__()
        self.assertIn("[User] (987654)", usr_str)
        self.assertIn("'id': '987654'", usr_str)
        self.assertIn("'created_at': " + _dt_rep, usr_str)
        self.assertIn("'updated_at': " + _dt_rep, usr_str)

    def test_2_diff_created_at(self):
        usr_1 = User()
        sleep(0.05)
        usr_2 = User()
        self.assertLess(usr_1.created_at, usr_2.created_at)

    def test_2_diff_updt_at(self):
        usr_1 = User()
        sleep(0.05)
        usr_2 = User()
        self.assertLess(usr_1.updated_at, usr_2.updated_at)

    def test_first_name_pub_str(self):
        usr_fn = User.first_name
        self.assertEqual(str, type(usr_fn))

    def test_last_name_pub_str(self):
        usr_ln = User.last_name
        self.assertEqual(str, type(usr_ln))

    def test_email_pub_str(self):
        usr_email = User.email
        self.assertEqual(str, usr_email)

    def test_password_pub_str(self):
        usr_pw = User.password
        self.assertEqual(str, type(usr_pw))

    def test_unused_args(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            User(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        usr = User(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(usr.id, "456")
        self.assertEqual(usr.created_at, _dt)
        self.assertEqual(usr.updated_at, _dt)


if __name__ == "__main__":
    unittest.main()
