#!/usr/bin/python3
"""
Module for testing the File Storage system in the models package.
"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """
    Class to perform unit tests on the File Storage mechanism.
    """

    def setUp(self):
        """
        Set up the test environment by clearing the __objects dictionary.
        """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def test_obj_list_empty(self):
        """
        Confirm that the __objects dictionary is initially empty.
        """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """
        Ensure a new object is correctly added to the __objects dictionary.
        """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """
        Confirm that the __objects dictionary is properly returned.
        """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_empty(self):
        """
        Confirm that data is saved to the file.
        """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """
        Test the FileStorage save method.
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        Ensure that the storage file is successfully loaded to __objects.
        """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_from_nonexistent(self):
        """
        Confirm that nothing happens if the file does not exist during reload.
        """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """
        Confirm that the BaseModel save method calls the storage save method.
        """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """
        Verify that __file_path is of type string.
        """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """
        Confirm that __objects is of type dict.
        """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """
        Verify that the key is properly formatted.
        """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """
        Confirm that the FileStorage object 'storage' is created.
        """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
