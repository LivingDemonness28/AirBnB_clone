#!/usr/bin/python3
"""unittests for User.py

unnitest classes:
    TestHBNBCmdAll
    TestHBNBCmdCreate
    TestHBNBCmdDestroy
    TestHBNBCmdExit
    TestHBNBCmdHelp
    TestHBNBCmdPrompting
    TestHBNBCmdShow
    TestHBNBCmdUpdate
"""
import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage

list1 = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]
list2 = ["Amenity", "City", "Place", "Review", "State", "User"]


class TestHBNBCmdAll(unittest.TestCase):
    """unittest: testing all of HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_single_dot_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_single_space_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_dot_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())

    def test_space_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())

    def test_inv_cls(self):
        i = "** class does not exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(i, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(i, output.getvalue().strip())


class TestHBNBCmdCreate(unittest.TestCase):
    """unittest: testing create of HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_obj(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            with patch("sys.stdout", new=StringIO()) as output:
                j = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd("create " + list1[i]))
                self.assertLess(0, len(j))
                tk = f"{list1[i]}.{j}"
                self.assertIn(tk, storage.all().keys())
            i = i + 1

    def test_inv_cls(self):
        i = "** class does not exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(i, val)

    def test_missing_cls(self):
        i = "** missing class name **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(i, val)

    def test_inv_syntax(self):
        i = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(i, val)
        j = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(j, val)


class TestHBNBCmdDestroy(unittest.TestCase):
    """unittest: testing destroy of HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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
        storage.reload()

    def test_dot_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create " + j))
                t_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                o = storage.all()[f"{j}.{t_id}"]
                _cmd = f"destroy {j} {t_id}"
                self.assertFalse(HBNBCommand().onecmd(_cmd))
                self.assertNotIn(o, storage.all())
            i = i + 1

    def test_space_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create " + j))
                t_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                o = storage.all()[j + f".{t_id}"]
                _cmd = j + f".destroy({t_id})"
                self.assertFalse(HBNBCommand().onecmd(_cmd))
                self.assertNotIn(o, storage.all())
            i = i + 1

    def test_inv_id_dot_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(j + ".destroy(1)"))
                self.assertEqual(i, output.getvalue().strip())
            j = j + 1

    def test_inv_id_space_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy " + j + " 1"))
                self.assertEqual(i, output.getvalue().strip())
            j = j + 1

    def test_id_missing_dot_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(j + ".destroy()"))
                self.assertEqual(i, output.getvalue().strip())
            j = j + 1

    def test_inv_id_space_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy " + j))
                self.assertEqual(i, output.getvalue().strip())
            j = j + 1

    def test_inv_cls(self):
        i = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(i, val)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(i, val)

    def test_missing_cls(self):
        i = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(i, val)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(i, val)


class TestHBNBCmdExit(unittest.TestCase):
    """unittest: testing exit of HBNB command interpreter"""

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCmdHelp(unittest.TestCase):
    """unittest: testing help of HBNB command interpreter"""

    def test_all(self):
        str1 = "Usage: all or all <class> or <class>.all()\n        "
        str2 = "Display string representations of all instances of "
        str3 = "a given class"
        str4 = ".\n       If no class is specified, displays all instantiated "
        str5 = "objects."
        _help = (str1 + str2 + str3 + str4 + str5)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(_help, val)

    def test_count(self):
        str1 = "Usage: count <class> or <class>.count()\n        "
        str2 = "Retrieve the number of instances of a given class."
        _help = (str1 + str2)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(_help, val)

    def test_create(self):
        str1 = "Usage: create <class>\n        "
        str2 = "Create a new class instance and print its id."
        _help = (str1 + str2)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(_help, val)

    def test_help_destroy(self):
        str1 = "Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
        str2 = "Delete a class instance of a given id."
        _help = (str1 + str2)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(_help, val)

    def test_help_EOF(self):
        _help = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(_help, val)

    def test_help(self):
        str1 = "Documented commands (type help <topic>):\n"
        str2 = "========================================\n"
        str3 = "EOF  all  count  create  destroy help  quit  show  update"
        _help = (str1 + str2 + str3)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(_help, val)

    def test_quit(self):
        _help = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(_help, val)

    def test_show(self):
        str1 = "Usage: show <class> <id> or <class>.show(<id>)\n        "
        str2 = "Display the string representation of a class instance of"
        str3 = " a given id."
        _help = (str1 + str2 + str3)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(_help, val)

    def test_updt(self):
        str1 = "Usage: update <class> <id> "
        str2 = "<attribute_name> <attribute_value> or"
        str3 = "\n       <class>.update(<id>, "
        str4 = "<attribute_name>, <attribute_value"
        str5 = ">) or\n       <class>.update(<id>, <dictionary>)\n        "
        str6 = "Update a class instance of a "
        str7 = "given id by adding or updating\n   "
        str8 = "     a given attribute key/value pair or dictionary."
        _help = (str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(_help, val)


class TestHBNBCmdPrompting(unittest.TestCase):
    """unittest: testing prompting of HBNB command interpreter"""

    def test_el(self):
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", val)

    def test_str(self):
        _prompt = HBNBCommand.prompt
        self.assertEqual("(hbnb) ", _prompt)


class TestHBNBCmdShow(unittest.TestCase):
    """unittest: testing show of HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_dot_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create " + j))
                t_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                o = storage.all()[j + f".{t_id}"]
                val = output.getvalue().strip()
                _cmd = j + f".show({t_id})"
                self.assertFalse(HBNBCommand().onecmd(_cmd))
                self.assertEqual(o.__str__(), val)
            i = i + 1

    def test_space_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create " + j))
                t_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                o = storage.all()[j + f".{t_id}"]
                val = output.getvalue().strip()
                _cmd = "show " + j + f" {t_id}"
                self.assertFalse(HBNBCommand().onecmd(_cmd))
                self.assertEqual(o.__str__(), val)
            i = i + 1

    def test_no_inst_found_dot_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd(j + ".show(1)"))
                self.assertEqual(i, val)
            i = i + 1

    def test_no_inst_found_space_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd("show " + j + " 1"))
                self.assertEqual(i, val)
            i = i + 1

    def test_missing_id_not(self):
        i = "** instance id missing **"
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd(j + ".show()"))
                self.assertEqual(i, val)
            i = i + 1

    def test_no_inst_found_space_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd("show " + j))
                self.assertEqual(i, val)
            i = i + 1

    def test_missing_cls(self):
        i = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(i, val)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(i, val)

    def test_inv_cls(self):
        i = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(i, val)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(i, val)


class TestHBNBCmdUpdate(unittest.TestCase):
    """unittest: testing update of HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_val_dict_flt_dot_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = f"Place.update({_t_id}, "
        _t_cmd = _t_cmd + "{'latitude': 9.8})"
        HBNBCommand().onecmd(_t_cmd)
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_val_dict_flt_space_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = f"update Place {_t_id} "
        _t_cmd = _t_cmd + "{'latitude': 9.8}"
        HBNBCommand().onecmd(_t_cmd)
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_val_dict_int_dot_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = f"Place.update({_t_id}, "
        _t_cmd = _t_cmd + "{'max_guest': 98})"
        HBNBCommand().onecmd(_t_cmd)
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(9.8, test_dict["max_guest"])

    def test_val_dict_int_space_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = f"update Place {_t_id} "
        _t_cmd = _t_cmd + "{'max_guest': 98}"
        HBNBCommand().onecmd(_t_cmd)
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(9.8, test_dict["max_guest"])

    def test_val_dict_dot_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + j)
                _t_id = output.getvalue().strip()
            _t_cmd = j + f".update({_t_id}, "
            _t_cmd = _t_cmd + "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(_t_cmd)
            test_dict = storage.all()[f"Place.{_t_id}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])
            i = i + 1

    def test_val_dict_space_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + j)
                _t_id = output.getvalue().strip()
            _t_cmd = "update " + j + f" {_t_id} "
            _t_cmd = _t_cmd + "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(_t_cmd)
            test_dict = storage.all()[f"Place.{_t_id}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])
            i = i + 1

    def test_val_flt_attr_dot_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = f"Place.update({_t_id}, "
        _t_cmd = _t_cmd + "latitude, 7.2)"
        self.assertFalse(HBNBCommand().onecmd(_t_cmd))
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_val_flt_attr_space_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = "update Place " + f"{_t_id} "
        _t_cmd = _t_cmd + "latitude 7.2"
        self.assertFalse(HBNBCommand().onecmd(_t_cmd))
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_val_int_attr_dot_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = f"Place.update({_t_id}, "
        _t_cmd = _t_cmd + "max_guest, 72)"
        self.assertFalse(HBNBCommand().onecmd(_t_cmd))
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(72, test_dict["max_guest"])

    def test_val_int_attr_space_not(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            _t_id = output.getvalue().strip()
        _t_cmd = "update Place " + f"{_t_id} "
        _t_cmd = _t_cmd + "max_guest 72"
        self.assertFalse(HBNBCommand().onecmd(_t_cmd))
        test_dict = storage.all()[f"Place.{_t_id}"].__dict__
        self.assertEqual(72, test_dict["max_guest"])

    def test_val_str_attr_dot_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + j)
                _t_id = output.getvalue().strip()
            _t_cmd = j + f".update({_t_id}, "
            _t_cmd = _t_cmd + "attr_name, 'attr_value')"
            self.assertFalse(HBNBCommand().onecmd(_t_cmd))
            test_dict = storage.all()[j + f".{_t_id}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])
            i = i + 1

    def test_val_str_attr_space_not(self):
        len1 = len(list1)
        i = 0

        while i < len1:
            j = list1[i]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create " + j)
                _t_id = output.getvalue().strip()
            _t_cmd = "update " + j + f"{_t_id} "
            _t_cmd = _t_cmd + "attr_name 'attr_value'"
            self.assertFalse(HBNBCommand().onecmd(_t_cmd))
            _t_dict = storage.all()[j + f".{_t_id}"].__dict__
            self.assertEqual("attr_value", _t_dict["attr_name"])
            i = i + 1

    def test_missing_attr_value_dot_not(self):
        i = "** value missing **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create" + k)
                _t_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                _t_cmd = k + f".update({_t_id}, attr_name)"
                self.assertFalse(HBNBCommand().onecmd(_t_cmd))
                self.assertEqual(i, val)
            j = j + 1

    def test_missing_attr_value_space_not(self):
        i = "** value missing **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create" + k)
                _t_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                _t_cmd = "update" + k + f" {_t_id} attr_name"
                self.assertFalse(HBNBCommand().onecmd(_t_cmd))
                self.assertEqual(i, val)
            j = j + 1

    def test_missing_attr_name_dot_not(self):
        i = "** value missing **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create" + k))
                _t_id = output.getvalue().strip()
                _t_cmd = k + f".update({_t_id})"
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd(_t_cmd))
                self.assertEqual(i, val)
            j = j + 1

    def test_missing_attr_name_space_not(self):
        i = "** value missing **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create" + k))
                _t_id = output.getvalue().strip()
                _t_cmd = "update " + k + f"{_t_id}"
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd(_t_cmd))
                self.assertEqual(i, val)
            j = j + 1

    def test_inv_id_dot_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd(k + ".update(1)"))
                self.assertEqual(i, val)
            j = j + 1

    def test_inv_id_space_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd("update " + k + " 1"))
                self.assertEqual(i, val)
            j = j + 1

    def test_missing_id_dot_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd(k + ".update()"))
                self.assertEqual(i, val)
            j = j + 1

    def test_inv_id_space_not(self):
        i = "** no instance found **"
        len1 = len(list1)
        j = 0

        while j < len1:
            k = list1[j]
            with patch("sys.stdout", new=StringIO()) as output:
                val = output.getvalue().strip()
                self.assertFalse(HBNBCommand().onecmd("update " + k))
                self.assertEqual(i, val)
            j = j + 1

    def test_update_missing_class(self):
        i = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(i, val)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(i, val)

    def test_update_invalid_class(self):
        i = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(i, val)
        with patch("sys.stdout", new=StringIO()) as output:
            val = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(i, val)


if __name__ == "__main__":
    unittest.main()
