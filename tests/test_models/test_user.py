#!/usr/bin/python3
"""
Here, we're diving into the world of TestUserDocs classes. Buckle up!
"""

import unittest
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
from models import user

User = user.User


class TestUser(unittest.TestCase):
    """
    Testing the User class
    """

    def test_str(self):
        """
        Checking if the str method has the right vibe
        """
        user_instance = User()
        string = "[User] ({}) {}".format(user_instance.id,
                                         user_instance.__dict__)
        self.assertEqual(string, str(user_instance))

    def test_to_dict_values(self):
        """
        Ensuring values in the dict returned from
        to_dict are on point
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_dict = u.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         u.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         u.updated_at.strftime(t_format))

    def test_to_dict_creates_dict(self):
        """
        Making sure to_dict method crafts
        a dictionary with the right vibes
        """
        u = User()
        new_dict = u.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in u.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_last_name_attr(self):
        """
        Checking if User rocks the 'last_name' attribute,
        and it's an empty string
        """
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "last_name"))
        if models.storage == 'db':
            self.assertEqual(user_instance.last_name, None)
        else:
            self.assertEqual(user_instance.last_name, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_first_name_attr(self):
        """
        Checking if User rocks the 'first_name' attribute,
        and it's an empty string
        """
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "first_name"))
        if models.storage == 'db':
            self.assertEqual(user_instance.first_name, None)
        else:
            self.assertEqual(user_instance.first_name, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_password_attr(self):
        """
        Checking if User rocks the 'password' attribute,
        and it's an empty string
        """
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "password"))
        if models.storage == 'db':
            self.assertEqual(user_instance.password, None)
        else:
            self.assertEqual(user_instance.password, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_email_attr(self):
        """
        Checking if User rocks the 'email' attribute,
        and it's an empty string
        """
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "email"))
        if models.storage == 'db':
            self.assertEqual(user_instance.email, None)
        else:
            self.assertEqual(user_instance.email, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_is_subclass(self):
        """
        Confirming that User is a cool subclass of BaseModel
        """
        user_instance = User()
        self.assertIsInstance(user_instance, BaseModel)
        self.assertTrue(hasattr(user_instance, "id"))
        self.assertTrue(hasattr(user_instance, "created_at"))
        self.assertTrue(hasattr(user_instance, "updated_at"))


class TestUserDocs(unittest.TestCase):
    """
    Tests to make sure the documentation and style of
    User class are on point
    """

    @classmethod
    def setUpClass(cls):
        """
        Setting the stage for the doc tests
        """
        cls.user_functions = inspect.getmembers(User, inspect.isfunction)

    def test_user_func_docstrings(self):
        """
        Checking if User methods have the right amount
        of swag in their docstrings
        """
        for func in self.user_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring, my friend!"
                             .format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring, my friend!"
                            .format(func[0]))

    def test_user_class_docstring(self):
        """
        Ensuring User class has a proper docstring
        """
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring, my friend!")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring, my friend!")

    def test_user_module_docstring(self):
        """
        Making sure user.py module is not missing out on
        the docstring fun
        """
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring, my friend!")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring, my friend!")


if __name__ == "__main__":
    unittest.main()
