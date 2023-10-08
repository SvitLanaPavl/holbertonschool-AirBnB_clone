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

    def test_new(self):
        """Testing new() method"""
        new_obj = BaseModel()
        key = f"{new_obj.__class__.__name__}.{new_obj.id}"
        self.assertIn(key, self.storage.all())

    def test_new_more_args(self):
        """testing new() by passing more args"""
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_save_and_reload(self):
        """Testing save() and reload() methods"""
        new_storage = BaseModel()
        self.storage.new(new_storage)
        self.storage.save()
        text = ""
        with open("temp_file.json", "r") as json_file:
            text = json_file.read()
            self.assertIn("BaseModel." + new_storage.id, text)
        self.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + new_storage.id, obj)

    def test_save_args(self):
        """testing save() method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.save(1)

    def test_reload_args(self):
        """testing save() method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(1)

    if __name__ == "__main__":
        unittest.main()
