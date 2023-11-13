#!/usr/bin/python3
"""
This script contains the TestReviewDocs classes for testing Review class.
"""

import unittest
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
from models import review

Review = review.Review


class TestReview(unittest.TestCase):
    """
    Testing the Review class
    """

    def test_str(self):
        """
        Checking if the str method flaunts the right output
        """
        review_instance = Review()
        string = "[Review] ({}) {}".format(review_instance.id,
                                           review_instance.__dict__)
        self.assertEqual(string, str(review_instance))

    def test_to_dict_values(self):
        """
        Ensuring values in the dict returned from
        to_dict are on point
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_dict = r.to_dict()
        self.assertEqual(new_dict["__class__"], "Review")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         r.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         r.updated_at.strftime(t_format))

    def test_to_dict_creates_dict(self):
        """
        Making sure to_dict method crafts
        a dictionary with the right vibes
        """
        r = Review()
        new_dict = r.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in r.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_text_attr(self):
        """
        Checking if Review rocks the 'text' attribute,
        and it's an empty string
        """
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "text"))
        if models.storage == 'db':
            self.assertEqual(review_instance.text, None)
        else:
            self.assertEqual(review_instance.text, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_user_id_attr(self):
        """
        Ensuring Review has the 'user_id' attribute,
        and it's an empty string
        """
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "user_id"))
        if models.storage == 'db':
            self.assertEqual(review_instance.user_id, None)
        else:
            self.assertEqual(review_instance.user_id, "")

    @unittest.skipIf(models.storage == 'db', "not testing File Storage")
    def test_place_id_attr(self):
        """
        Verifying Review has the 'place_id' attribute,
        and it's an empty string
        """
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "place_id"))
        if models.storage == 'db':
            self.assertEqual(review_instance.place_id, None)
        else:
            self.assertEqual(review_instance.place_id, "")

    def test_is_subclass(self):
        """
        Confirming that Review is a cool subclass of BaseModel
        """
        review_instance = Review()
        self.assertIsInstance(review_instance, BaseModel)
        self.assertTrue(hasattr(review_instance, "id"))
        self.assertTrue(hasattr(review_instance, "created_at"))
        self.assertTrue(hasattr(review_instance, "updated_at"))


class TestReviewDocs(unittest.TestCase):
    """
    Tests to make sure the documentation and
    style of Review class are on point
    """

    @classmethod
    def setUpClass(cls):
        """
        Getting ready for the doc tests!
        """
        cls.review_functions = inspect.getmembers(Review,
                                                  inspect.isfunction)

    def test_review_func_docstrings(self):
        """
        Checking if Review methods have the
        right amount of swag in their docstrings
        """
        for func in self.review_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring, my friend!"
                             .format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring, my friend!"
                            .format(func[0]))

    def test_review_class_docstring(self):
        """
        Ensuring Review class has a proper docstring
        """
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring, my friend!")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring, my friend!")

    def test_review_module_docstring(self):
        """
        Making sure review.py module is not missing out
        on the docstring fun
        """
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring, my friend!")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring, my friend!")


if __name__ == "__main__":
    unittest.main()
