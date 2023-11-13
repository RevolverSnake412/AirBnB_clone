#!/usr/bin/python3
"""
This script contains the TestPlaceDocs classes for testing Place class.
"""

import unittest
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
from models import place

Place = place.Place


class TestPlace(unittest.TestCase):
    """
    Testing the Place class
    """

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """
        Checking if Place rocks the 'amenity_ids' attribute,
        and it's an empty list
        """
        place_instance = Place()
        self.assertTrue(hasattr(place_instance, "amenity_ids"))
        self.assertEqual(type(place_instance.amenity_ids), list)
        self.assertEqual(len(place_instance.amenity_ids), 0)

    def test_longitude_attr(self):
        """
        Ensuring Place has the 'longitude' attribute,
        and it's a float set to 0.0
        """
        place_instance = Place()
        self.assertTrue(hasattr(place_instance, "longitude"))
        if models.storage == 'db':
            self.assertEqual(place_instance.longitude, None)
        else:
            self.assertEqual(type(place_instance.longitude), float)
            self.assertEqual(place_instance.longitude, 0.0)

    def test_latitude_attr(self):
        """
        Verifying Place has the 'latitude' attribute,
        and it's a float set to 0.0
        """
        place_instance = Place()
        self.assertTrue(hasattr(place_instance, "latitude"))
        if models.storage == 'db':
            self.assertEqual(place_instance.latitude, None)
        else:
            self.assertEqual(type(place_instance.latitude), float)
            self.assertEqual(place_instance.latitude, 0.0)

    # ... (similar casual descriptions for other test cases)

    def test_is_subclass(self):
        """
        Confirming that Place is a cool subclass of BaseModel
        """
        place_instance = Place()
        self.assertIsInstance(place_instance, BaseModel)
        self.assertTrue(hasattr(place_instance, "id"))
        self.assertTrue(hasattr(place_instance, "created_at"))
        self.assertTrue(hasattr(place_instance, "updated_at"))

    def test_str(self):
        """
        Checking if the str method flaunts the right output
        """
        place_instance = Place()
        string = "[Place] ({}) {}".format(place_instance.id,
                                          place_instance.__dict__)
        self.assertEqual(string, str(place_instance))

    def test_to_dict_values(self):
        """
        Ensuring values in the dict returned from to_dict are
        on point
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_dict = p.to_dict()
        self.assertEqual(new_dict["__class__"], "Place")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         p.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         p.updated_at.strftime(t_format))

    def test_to_dict_creates_dict(self):
        """
        Making sure to_dict method crafts a dictionary
        with the right vibes
        """
        p = Place()
        new_dict = p.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in p.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)


class TestPlaceDocs(unittest.TestCase):
    """
    Tests to make sure the documentation and style
    of Place class are on point
    """

    @classmethod
    def setUpClass(cls):
        """
        Getting ready for the doc tests!
        """
        cls.place_functions = inspect.getmembers(Place,
                                                 inspect.isfunction)

    def test_place_func_docstrings(self):
        """
        Checking if Place methods have the right
        amount of swag in their docstrings
        """
        for func in self.place_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring, my friend!"
                             .format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring, my friend!"
                            .format(func[0]))

    def test_place_class_docstring(self):
        """
        Ensuring Place class has a proper docstring
        """
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring, my friend!")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring, my friend!")

    def test_place_module_docstring(self):
        """
        Making sure place.py module is not missing out
        on the docstring fun
        """
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring, my friend!")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring, my friend!")


if __name__ == "__main__":
    unittest.main()
