#!/usr/bin/python3
"""A base_model.py class"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    The base model class that defines all
    attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Init"""
        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        prints representation of the cladd
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        data of __dict__ instance
        """
        objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                objects[key] = value.isoformat()
            else:
                objects[key] = value
        objects["__class__"] = self.__class__.__name__
        return objects
