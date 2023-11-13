#!/usr/bin/python3
"""
This script contains the TestCityDocs classes for testing City class.
"""

import unittest
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
from models import city

City = city.City


class TestCity(unittest.TestCase):
    """
    Testing the City class
    """

    def test_str(self):
        """
        Checking if the str method does its magic
        """
        city_instance = City()
        string = "[City] ({}) {}".format(city_instance.id,
                                         city_instance.__dict__)
        self.assertEqual(string, str(city_instance))

    def test_to_dict_values(self):
        """
        Ensuring values in the dict returned
        from to_dict are spot-on
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_dict = c.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         c.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         c.updated_at.strftime(t_format))

    def test_to_dict_creates_dict(self):
        """
        Making sure to_dict method crafts a
        dictionary with the right vibes
        """
        c = City()
        new_dict = c.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in c.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_state_id_attr(self):
        """
        Checking if City rocks the 'state_id' attribute,
        and it's an empty string
        """
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "state_id"))
        if models.storage == 'db':
            self.assertEqual(city_instance.state_id, None)
        else:
            self.assertEqual(city_instance.state_id, "")

    def test_name_attr(self):
        """
        Ensuring City has the 'name' attribute,
        and it's an empty string
        """
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "name"))
        if models.storage == 'db':
            self.assertEqual(city_instance.name, None)
        else:
            self.assertEqual(city_instance.name, "")

    def test_is_subclass(self):
        """
        Confirming that City is a cool subclass of BaseModel
        """
        city_instance = City()
        self.assertIsInstance(city_instance, BaseModel)
        self.assertTrue(hasattr(city_instance, "id"))
        self.assertTrue(hasattr(city_instance, "created_at"))
        self.assertTrue(hasattr(city_instance, "updated_at"))


class TestCityDocs(unittest.TestCase):
    """
    Tests to make sure the documentation and
    style of City class are on point
    """

    @classmethod
    def setUpClass(cls):
        """
        Getting ready for the doc tests!
        """
        cls.city_functions = inspect.getmembers(City,
                                                inspect.isfunction)

    def test_city_func_docstrings(self):
        """
        Checking if City methods have the right
        amount of swag in their docstrings
        """
        for func in self.city_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring,my friend!"
                             .format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring, my friend!"
                            .format(func[0]))

    def test_city_class_docstring(self):
        """
        Ensuring City class has a proper docstring
        """
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring, my friend!")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring, my friend!")

    def test_city_module_docstring(self):
        """
        Making sure city.py module is not missing out
        on the docstring fun
        """
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring, my friend!")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring, my friend!")


if __name__ == "__main__":
    unittest.main()
