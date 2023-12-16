#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """Represents storage engine.

    Returns:
        __file_path (str): File name to save objects to.
        __objects (dict): Dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        sdict = FileStorage.__objects
        ssdict = {obj: sdict[obj].to_dict() for obj in sdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ssdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as file:
                ssdict = json.load(file)
                for o in ssdict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            pass
