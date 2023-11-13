#!/usr/bin/python3
"""
This script contains the TestAmenityDocs classes for testing Amenity class.
"""

import unittest
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
from models import amenity

Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """
    Let's put Amenity to the test!
    """

    def test_name_amenity(self):
        """
        Name desc
        """
        amenity = Amenity()
        amenity.name = "jacuzzi"
        self.assertEqual(amenity.name, "jacuzzi")

    def test_class_amenity(self):
        """
        The amenity class itself
        """
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_parent_class_amenity(self):
        """
        The parent class
        """
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))

    def test_amenity(self):
        """
        The Amenity's attributes
        """
        my_amenity = Amenity()
        my_amenity.name = "Kitchen"
        self.assertEqual(my_amenity.name, "Kitchen")

    def test_str_amenity(self):
        """
        Checks if the str method does its
        thing properly.
        """
        amenity_instance = Amenity()
        string = "[Amenity] ({}) {}".format(amenity_instance.id,
                                            amenity_instance.__dict__)
        self.assertEqual(string, str(amenity_instance))

    def test_to_dict_values_amenity(self):
        """
        Makes sure the values in the dict returned
        from to_dict are on point.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         am.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         am.updated_at.strftime(t_format))

    def test_to_dict_creates_dict_amenity(self):
        """
        Checks if to_dict method crafts a dictionary
        with the right attributes
        """
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_name_attr_amenity(self):
        """
        Ensures Amenity has the 'name' attribute,
        and it's an empty string
        """
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, "name"))
        if models.storage == 'db':
            self.assertEqual(amenity_instance.name, None)
        else:
            self.assertEqual(amenity_instance.name, "")

    def test_is_subclass_amenity(self):
        """
        Confirms that Amenity is a cool subclass
        of BaseModel
        """
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, BaseModel)
        self.assertTrue(hasattr(amenity_instance, "id"))
        self.assertTrue(hasattr(amenity_instance, "created_at"))
        self.assertTrue(hasattr(amenity_instance, "updated_at"))


class TestAmenityDocs(unittest.TestCase):
    """
    Tests to make sure the documentation and
    style of Amenity class are on point.
    """

    @classmethod
    def setUpClass(cls):
        """
        Getting ready for the doc tests!
        """
        cls.amenity_functions = inspect.getmembers(Amenity,
                                                   inspect.isfunction)

    def test_amenity_func_docstrings_amenity(self):
        """
        Checking if Amenity methods have
        the right amount of swag in their docstrings
        """
        for func in self.amenity_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring, my friend!"
                             .format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring, my friend!"
                            .format(func[0]))

    def test_amenity_class_docstring_amenity(self):
        """
        Ensuring Amenity class has a proper docstring
        """
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring, my friend!")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring, my friend!")

    def test_amenity_module_docstring_amenity(self):
        """
        Making sure amenity.py module is not missing
        out on the docstring fun
        """
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring, my friend!")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring, my friend!")


if __name__ == "__main__":
    unittest.main()
