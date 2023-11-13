#!/usr/bin/python3
"""
This script contains the TestStateDocs classes for testing State class.
"""

import unittest
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
from models import state

State = state.State


class TestState(unittest.TestCase):
    """
    Testing the State class
    """

    def test_str(self):
        """
        Checking if the str method flaunts the right output
        """
        state_instance = State()
        string = "[State] ({}) {}".format(state_instance.id,
                                          state_instance.__dict__)
        self.assertEqual(string, str(state_instance))

    def test_to_dict_values(self):
        """
        Ensuring values in the dict returned from
        to_dict are on point
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_dict = s.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         s.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         s.updated_at.strftime(t_format))

    def test_to_dict_creates_dict(self):
        """
        Making sure to_dict method crafts a dictionary
        with the right vibes
        """
        s = State()
        new_dict = s.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in s.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_name_attr(self):
        """
        Checking if State rocks the 'name' attribute,
        and it's an empty string
        """
        state_instance = State()
        self.assertTrue(hasattr(state_instance, "name"))
        if models.storage == 'db':
            self.assertEqual(state_instance.name, None)
        else:
            self.assertEqual(state_instance.name, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_is_subclass(self):
        """
        Confirming that State is a cool subclass of BaseModel
        """
        state_instance = State()
        self.assertIsInstance(state_instance, BaseModel)
        self.assertTrue(hasattr(state_instance, "id"))
        self.assertTrue(hasattr(state_instance, "created_at"))
        self.assertTrue(hasattr(state_instance, "updated_at"))


class TestStateDocs(unittest.TestCase):
    """
    Tests to make sure the documentation and style
    of State class are on point
    """

    @classmethod
    def setUpClass(cls):
        """
        Getting ready for the doc tests!
        """
        cls.state_functions = inspect.getmembers(State,
                                                 inspect.isfunction)

    def test_state_func_docstrings(self):
        """
        Checking if State methods have the right
        amount of swag in their docstrings
        """
        for func in self.state_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring, my friend!"
                             .format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring, my friend!"
                            .format(func[0]))

    def test_state_class_docstring(self):
        """
        Ensuring State class has a proper docstring
        """
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring, my friend!")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring, my friend!")

    def test_state_module_docstring(self):
        """
        Making sure state.py module is not missing out
        on the docstring fun
        """
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring, my friend!")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring, my friend!")


if __name__ == "__main__":
    unittest.main()
