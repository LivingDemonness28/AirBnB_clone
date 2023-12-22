#!/usr/bin/python3
"""Defines the HBNBCommand console"""
import re
import cmd
from shlex import split
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


def scan(arg):
    """Extracts elem from string"""
    braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if brackets is None:
            res = []
            for i in split(arg):
                res.append(i.strip(","))
            return res
        else:
            prefix = split(arg[:brackets.span()[0]])
            ret_list = []
            for i in prefix:
                ret_list.append(i.strip(","))
            ret_list.append(brackets.group())
            return ret_list
    else:
        prefix = split(arg[:braces.span()[0]])
        ret_list = []
        for i in prefix:
            ret_list.append(i.strip(","))
        ret_list.append(braces.group())
        return ret_list


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    __cls = {
        "User",
        "Basemodel",
        "State",
        "Amenity",
        "City",
        "Place",
        "Review"
    }

    def do_destroy(self, arg):
        """Delete class instance of id given."""
        arg_list = scan(arg)
        o_dict = storage.all()
        len1 = len(arg_list)
        if len1 == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        elif len1 == 1:
            print("** instance id missing **")
        elif f"{arg_list[0]}.{arg_list[1]}" not in o_dict.keys():
            print("** no instance found **")
        else:
            del o_dict[f"{arg_list[0]}.{arg_list[1]}"]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all instances of given class.
        If no class specified, displays all instantiated objects."""
        arg_list = scan(arg)
        len1 = len(arg_list)
        if (len1 > 0) and (arg_list[0] not in HBNBCommand.__cls):
            print("** class doesn't exist **")
        else:
            obj_list = []
            for i in storage.all().values():
                len2 = len(arg_list)
                if (len2 > 0) and (arg_list == i.__class__.__name__):
                    obj_list.append(i.__str__())
                elif len2 == 0:
                    obj_list.append(i.__str__())
                print(obj_list)

    def do_count(self, arg):
        """Retrieve num of instances of given class"""
        arg_list = scan(arg)
        total = 0
        for i in storage.all().values():
            if arg_list[0] == i.__class__.__name__:
                total = total + 1
            print(total)

    def do_show(self, arg):
        """Display str representation of class instance of given id"""
        arg_list = scan(arg)
        o_dict = storage.all()
        len1 = len(arg_list)
        if len1 == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__cls:
            print("** class does not exist **")
        elif len1 == 1:
            print("** instance id missing **")
        elif f"{arg_list[0]}.{arg_list[1]}" not in o_dict:
            print("** no instance found **")
        else:
            print(o_dict[f"{arg_list[0]}.{arg_list[1]}"])

    def do_update(self, arg):
        """update class instance of given id:
        add or update given attr k/v pair or dict"""
        arg_list = scan(arg)
        o_dict = storage.all()
        len1 = len(arg_list)

        if len1 == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
            return False
        if len1 == 1:
            print("** instance id missing ***")
            return False
        if len1 == 2:
            print("** attribute name missing **")
            return False
        if len1 == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len1 == 4:
            o = o_dict[f"{arg_list[0]}.{arg_list[1]}"]
            if arg_list[2] in o.__class__.__dict__.keys():
                vt = type(o.__class__.__dict__[arg_list[2]])
                o.__dict__[arg_list[2]] = vt(arg_list[3])
            else:
                o.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            o = o_dict[f"{arg_list[0]}.{arg_list[1]}"]
            for key, val in eval(arg_list[2]).items():
                i = o.__class__.__dict__
                if (key in i.keys() and type(i[key]) in {str, int, float}):
                    vt = type(i[key])
                    o.__dict__[key] = vt(val)
                else:
                    o.__dict__[key] = val
        storage.save()

    def default(self, arg):
        arg_dict = {
            "destroy": self.do_destroy,
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                _cmd = [arg_list[1][match.span()[0]], match.group()[1:-1]]
                if _cmd[0] in arg_dict.keys():
                    call = f"{arg_list[0]} {_cmd[1]}"
                    return arg_dict[_cmd[0]](call)
        print(f"*** Unknown syntax: {arg}")
        return False

    def do_create(self, arg):
        """create new class instance and print id"""
        arg_list = scan(arg)
        len1 = len(arg_list)
        if len1 == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_quit(self, arg):
        """exit program command"""
        return True

    def do_EOF(self, arg):
        """Exit the program EOF(ctrl-D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
