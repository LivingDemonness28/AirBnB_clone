#!/usr/bin/python3
"""unittests for cityity.py

unnitest classes:
    TestStateSave
    TestStateToDict
    TestStateInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.state import State


class TestStateSave(unittest.TestCase):
    """unittest: testing save method State class"""

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
        state = State()
        state.save()
        amid = "State." + state.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_one(self):
        state = State()
        sleep(0.05)
        updated_at_1 = state.updated_at
        state.save()
        self.assertLess(updated_at_1, state.updated_at)

class TestStateToDict(unittest.TestCase):
    """unittest: testing to_dict method State class"""

    def test_output(self):
        _dt = datetime.now()
        state = State()
        state.id = "987654"
        state.created_at = state.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'State',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), t_dict)

    def test_save(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_type(self):
        state_type = type(State().to_dict())
        self.assertTrue(dict, state_type)

    def test_added_attr(self):
        state = State()
        state.second_name = "ALX"
        state.num = 28
        state_dict = state.to_dict()
        self.assertEqual("ALX", state.second_name)
        self.assertIn("num", state_dict)

    def test_correct_keys(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

    def test_dt_attr_strs(self):
        state = State()
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict["id"], str))
        self.assertTrue(isinstance(state_dict["created_at"], str))
        self.assertTrue(isinstance(state_dict["updated_at"], str))

    def test_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)

    def test_dunder_dict(self):
        state = State()
        state_dict = state.to_dict()
        state_dd = state.__dict__
        self.assertNotEqual(state_dict, state_dd)

class TestStateInstantiation(unittest.TestCase):
    """unittest: testing instantiation of State class."""

    def test_id_pub_strs(self):
        state_id = State().id
        self.assertEqual(str, type(state_id))

    def test_created_at_pub_dt(self):
        state_ct = State().created_at
        self.assertEqual(datetime, type(state_ct))

    def test_updated_at_pub_dt(self):
        state_ut = State().updated_at
        self.assertEqual(datetime, type(state_ut))

    def test_2_state_uni_ids(self):
        state1_id = State().id
        state2_id = State().id
        self.assertNotEqual(state1_id, state2_id)

    def test_no_args_instantiate(self):
        state = State()
        self.assertEqual(State, type(state))

    def test_name_pub_cls_attr(self):
        state = State()
        state_name = State.name
        self.assertEqual(str, type(state_name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_stored_in_obj(self):
        self.assertIn(State(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        state = State()
        state.id = "987654"
        state.created_at = state.updated_at = _dt
        state_str = state.__str__()
        self.assertIn("[State] (987654)", state_str)
        self.assertIn("'id': '987654'", state_str)
        self.assertIn("'created_at': " + _dt_rep, state_str)
        self.assertIn("'updated_at': " + _dt_rep, state_str)

    def test_2_diff_created_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.created_at, state_2.created_at)

    def test_2_diff_updt_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.updated_at, state_2.updated_at)

    def test_unused_args(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            State(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        state = State(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(state.id, "456")
        self.assertEqual(state.created_at, _dt)
        self.assertEqual(state.updated_at, _dt)


if __name__ == "__main__":
    unittest.main()
