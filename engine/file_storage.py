#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel


class FileStorage:
    """"""
    def __init__(self):
        """Init"""
        self.__file_path = stockage.json
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
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        serializes the objects to JSON file
        (default JSON file = stockage.json)
        """
        with open(self.__file_path, 'w+') as fhand:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, fhand)

    def reload(self):
        """
        deserializes the JSON file to objects
        otherwise nothing happens
        """
        try:
            with open(self.__file_path, 'r') as fhand:
                dict = json.loads(fhand.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
