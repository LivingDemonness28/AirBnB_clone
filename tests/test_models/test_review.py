#!/usr/bin/python3
"""unittests for cityity.py

unnitest classes:
    TestReviewSave
    TestReviewToDict
    TestReviewInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.review import Review


class TestReviewSave(unittest.TestCase):
    """unittest: testing save method Review class"""

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
        rev = Review()
        rev.save()
        amid = "Review." + rev.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_one(self):
        rev = Review()
        sleep(0.05)
        updated_at_1 = rev.updated_at
        rev.save()
        self.assertLess(updated_at_1, rev.updated_at)

    def test_two(self):
        rev = Review()
        sleep(0.05)
        update_at_1 = rev.updated_at
        rev.save()
        update_at_2 = rev.updated_at
        self.assertLess(update_at_1, update_at_2)
        sleep(0.05)
        rev.save()
        self.assertLess(update_at_2, rev.updated_at)

class TestReviewToDict(unittest.TestCase):
    """unittest: testing to_dict method Review class"""

    def test_output(self):
        _dt = datetime.now()
        rev = Review()
        rev.id = "987654"
        rev.created_at = rev.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'Review',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), t_dict)

    def test_type(self):
        rev_type = type(Review().to_dict())
        self.assertTrue(dict, rev_type)

    def test_added_attr(self):
        rev = Review()
        rev.second_name = "ALX"
        rev.num = 28
        rev_dict = rev.to_dict()
        self.assertEqual("ALX", rev.second_name)
        self.assertIn("num", rev_dict)

    def test_correct_keys(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertIn("id", rev_dict)
        self.assertIn("created_at", rev_dict)
        self.assertIn("updated_at", rev_dict)
        self.assertIn("__class__", rev_dict)

    def test_dt_attr_strs(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertTrue(isinstance(rev_dict["id"], str))
        self.assertTrue(isinstance(rev_dict["created_at"], str))
        self.assertTrue(isinstance(rev_dict["updated_at"], str))

    def test_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)

    def test_dunder_dict(self):
        rev = Review()
        rev_dict = rev.to_dict()
        rev_dd = rev.__dict__
        self.assertNotEqual(rev_dict, rev_dd)

class TestReviewInstantiation(unittest.TestCase):
    """unittest: testing instantiation of Review class."""

    def test_id_pub_strs(self):
        rev_id = Review().id
        self.assertEqual(str, type(rev_id))

    def test_created_at_pub_dt(self):
        rev_ct = Review().created_at
        self.assertEqual(datetime, type(rev_ct))

    def test_updated_at_pub_dt(self):
        rev_ut = Review().updated_at
        self.assertEqual(datetime, type(rev_ut))

    def test_2_rev_uni_ids(self):
        rev1_id = Review().id
        rev2_id = Review().id
        self.assertNotEqual(rev1_id, rev2_id)

    def test_no_args_instantiate(self):
        rev = Review()
        self.assertEqual(Review, type(rev))

    def test_text_pub_cls_attr(self):
        rev = Review()
        rev_text = Review.text
        self.assertEqual(str, type(rev_text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_user_id_pub_cls_attr(self):
        rev = Review()
        rev_user_id = Review.user_id
        self.assertEqual(str, type(rev_user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_place_id_pub_cls_attr(self):
        rev = Review()
        rev_place_id = Review.place_id
        self.assertEqual(str, type(rev_place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_stored_in_obj(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        rev = Review()
        rev.id = "987654"
        rev.created_at = rev.updated_at = _dt
        rev_str = rev.__str__()
        self.assertIn("[Review] (987654)", rev_str)
        self.assertIn("'id': '987654'", rev_str)
        self.assertIn("'created_at': " + _dt_rep, rev_str)
        self.assertIn("'updated_at': " + _dt_rep, rev_str)

    def test_2_diff_created_at(self):
        rev_1 = Review()
        sleep(0.05)
        rev_2 = Review()
        self.assertLess(rev_1.created_at, rev_2.created_at)

    def test_2_diff_updt_at(self):
        rev_1 = Review()
        sleep(0.05)
        rev_2 = Review()
        self.assertLess(rev_1.updated_at, rev_2.updated_at)

    def test_unused_args(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        rev = Review(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(rev.id, "456")
        self.assertEqual(rev.created_at, _dt)
        self.assertEqual(rev.updated_at, _dt)


if __name__ == "__main__":
    unittest.main()
