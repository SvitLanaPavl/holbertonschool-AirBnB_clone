#!/usr/bin/python3
""" This Module contains UnitTests for the FileStorage Class """
import json
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestFileStorageAttributes(unittest.TestCase):
    """Testing basic instantiation and private class attributes"""

    def test_init_with_args(self):
        """trying to instantiate with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_type(self):
        """testing the type of the file path"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects_type(self):
        """testing the type of the file path"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

class TestFileStorageMethods(unittest.TestCase):
    """Testing file storage methods"""

    @classmethod
    def setUp(self):
        """Setting up test environment"""
        self.temp_file = "temp_file.json"
        FileStorage._FileStorage__file_path = self.temp_file
        self.storage = FileStorage()
        self.obj_1 = BaseModel()
        self.obj_2 = BaseModel()

    @classmethod
    def tearDown(self):
        """Removing the test environment"""
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_all(self):
        """Testing all() method"""
        all_obj = self.storage.all()
        self.assertIsInstance(all_obj, dict)
        self.assertIn(self.obj_1, all_obj.values())
        self.assertIn(self.obj_2, all_obj.values())

    def test_new(self):
        """Testing new() method"""
        new_obj = BaseModel()
        key = f"{new_obj.__class__.__name__}.{new_obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Testing save() and reload() methods"""
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), len(self.storage.all()))
        for key, obj in self.storage.all().items():
            self.assertTrue(key in new_storage.all())
            self.assertEqual(obj.to_dict(), new_storage.all()[key].to_dict())

    if __name__ == "__main__":
        unittest.main()
