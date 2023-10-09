#!/usr/bin/python3
""" This Module contains UnitTests for the FileStorage Class """
import json
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models import storage


class TestFileStorageAttributes(unittest.TestCase):
    """Testing basic instantiation and private class attributes"""

    def test_init_with_args(self):
        """trying to instantiate with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test_instantiation(self):
        """testing for the class name"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_class_type(self):
        """testing the type of the class"""
        self.assertEqual(type(FileStorage()), FileStorage)

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

    def test_all_None(self):
        """testing new() by passing None"""
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_all_excess_args(self):
        """testing new() by passing None"""
        with self.assertRaises(TypeError):
            self.storage.all(1)

    def test_new(self):
        """Testing new() method"""
        new_obj_bm = BaseModel()
        self.storage.new(new_obj_bm)
        key = f"{new_obj_bm.__class__.__name__}.{new_obj_bm.id}"
        self.assertIn(key, self.storage.all())

    def test_new_excess_args(self):
        """testing new() by passing more args"""
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_new_None(self):
        """testing new() by passing None"""
        with self.assertRaises(AttributeError):
            self.storage.new(None)

    def test_save_and_reload(self):
        """Testing save() and reload() methods"""
        new_storage_bm = BaseModel()
        self.storage.new(new_storage_bm)
        self.storage.save()
        text = ""
        with open("temp_file.json", "r") as json_file:
            text = json_file.read()
            self.assertIn("BaseModel." + new_storage_bm.id, text)
        self.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + new_storage_bm.id, obj)

    def test_save_args(self):
        """testing save() method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.save(1)

    def test_save_None(self):
        """testing save() method with passing None"""
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload_args(self):
        """testing reload() method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(1)

    def test_reload_None(self):
        """testing reload() method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(None)

    if __name__ == "__main__":
        unittest.main()
