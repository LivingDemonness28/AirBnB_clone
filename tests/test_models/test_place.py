#!/usr/bin/python3
"""unittests for cityity.py

unnitest classes:
    TestPlaceSave
    TestPlaceToDict
    TestPlaceInstantiation
"""
import unittest
import os
from time import sleep
from datetime import datetime
import models
from models.place import Place


class TestPlaceSave(unittest.TestCase):
    """unittest: testing save method Place class"""

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
        place = Place()
        place.save()
        amid = "Place." + place.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_one(self):
        place = Place()
        sleep(0.05)
        updated_at_1 = place.updated_at
        place.save()
        self.assertLess(updated_at_1, place.updated_at)

    def test_two(self):
        place = Place()
        sleep(0.05)
        update_at_1 = place.updated_at
        place.save()
        update_at_2 = place.updated_at
        self.assertLess(update_at_1, update_at_2)
        sleep(0.05)
        place.save()
        self.assertLess(update_at_2, place.updated_at)

class TestPlaceToDict(unittest.TestCase):
    """unittest: testing to_dict method Place class"""

    def test_output(self):
        _dt = datetime.now()
        place = Place()
        place.id = "987654"
        place.created_at = place.updated_at = _dt
        t_dict = {
            'id': '987654',
            '__class__': 'Place',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), t_dict)

    def test_save(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_type(self):
        place_type = type(Place().to_dict())
        self.assertTrue(dict, place_type)

    def test_added_attr(self):
        place = Place()
        place.second_name = "ALX"
        place.num = 28
        place_dict = place.to_dict()
        self.assertEqual("ALX", place.second_name)
        self.assertIn("num", place_dict)

    def test_correct_keys(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)

    def test_dt_attr_strs(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertTrue(isinstance(place_dict["id"], str))
        self.assertTrue(isinstance(place_dict["created_at"], str))
        self.assertTrue(isinstance(place_dict["updated_at"], str))

    def test_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)

    def test_dunder_dict(self):
        place = Place()
        place_dict = place.to_dict()
        place_dd = place.__dict__
        self.assertNotEqual(place_dict, place_dd)

class TestPlaceInstantiation(unittest.TestCase):
    """unittest: testing instantiation of Place class."""

    def test_id_pub_strs(self):
        place_id = Place().id
        self.assertEqual(str, type(place_id))

    def test_created_at_pub_dt(self):
        place_ct = Place().created_at
        self.assertEqual(datetime, type(place_ct))

    def test_updated_at_pub_dt(self):
        place_ut = Place().updated_at
        self.assertEqual(datetime, type(place_ut))

    def test_2_place_uni_ids(self):
        place1_id = Place().id
        place2_id = Place().id
        self.assertNotEqual(place1_id, place2_id)

    def test_no_args_instantiate(self):
        place = Place()
        self.assertEqual(Place, type(place))

    def test_user_id_pub_cls_attr(self):
        place = Place()
        place_user_id = Place.user_id
        self.assertEqual(str, type(place_user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_name_pub_cls_attr(self):
        place = Place()
        place_name = Place.name
        self.assertEqual(str, type(place_name))
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_city_id_pub_cls_attr(self):
        place = Place()
        place_city_id = Place.city_id
        self.assertEqual(str, type(place_city_id))
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_num_rooms_pub_cls_attr(self):
        place = Place()
        place_num_rooms = Place.number_rooms
        self.assertEqual(str, type(place_num_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_desc_pub_cls_attr(self):
        place = Place()
        place_desc = Place.description
        self.assertEqual(str, type(place_desc))
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_num_bthrm_pub_cls_attr(self):
        place = Place()
        place_bthrm = Place.number_bathrooms
        self.assertEqual(str, type(place_bthrm))
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_price_by_night_pub_cls_attr(self):
        place = Place()
        place_pbn = Place.price_by_night
        self.assertEqual(str, type(place_pbn))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_long_pub_cls_attr(self):
        place = Place()
        place_long = Place.longitude
        self.assertEqual(float, type(place_long))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_lat_pub_cls_attr(self):
        place = Place()
        place_lat = Place.latitude
        self.assertEqual(float, type(place_lat))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_max_guest_pub_cls_attr(self):
        place = Place()
        place_mg = Place.max_guest
        self.assertEqual(int, type(place_mg))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_amen_id_pub_cls_attr(self):
        place = Place()
        place_aid = Place.amenity_id
        self.assertEqual(list, type(place_aid))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

    def test_stored_in_obj(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_str(self):
        _dt = datetime.now()
        _dt_rep = repr(_dt)
        place = Place()
        place.id = "987654"
        place.created_at = place.updated_at = _dt
        place_str = place.__str__()
        self.assertIn("[Place] (987654)", place_str)
        self.assertIn("'id': '987654'", place_str)
        self.assertIn("'created_at': " + _dt_rep, place_str)
        self.assertIn("'updated_at': " + _dt_rep, place_str)

    def test_2_diff_created_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.created_at, place_2.created_at)

    def test_2_diff_updt_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.updated_at, place_2.updated_at)

    def test_unused_args(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id = None, created_at = None, updated_at = None)

    def test_ins_with_kwargs(self):
        _dt = datetime.now()
        _dt_iso = _dt.isoformat()
        place = Place(id="456", created_at = _dt_iso, updated_at = _dt_iso)
        self.assertEqual(place.id, "456")
        self.assertEqual(place.created_at, _dt)
        self.assertEqual(place.updated_at, _dt)


if __name__ == "__main__":
    unittest.main()
