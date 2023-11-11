#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """"""
    def __init__(self):
        """Init"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        returns the dictionary with objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in the object dictionary the
        key that is going to be the standard
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        serializes the objects to JSON file
        (default JSON file = stockage.json)
        """
        objects_dict = self.__objects
        obj_dict = {obj_key: obj.to_dict() for obj_key,
                    obj in objects_dict.items()}
        with open(self.__file_path, "w") as fhand:
            json.dump(obj_dict, fhand)

    def reload(self):
        """
        deserializes the JSON file to objects
        otherwise nothing happens
        """
        with open(self.__file_path, 'r') as fhand:
            obj_dict = json.load(fhand)
        for key in obj_dict:
            self.__objects[key] = classes[obj_dict[key]
                                          ["__class__"]](**obj_dict[key])
