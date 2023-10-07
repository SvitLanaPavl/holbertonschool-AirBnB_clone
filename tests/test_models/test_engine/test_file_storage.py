#!/usr/bin/python3
""" This Module contains UnitTests for the FileStorage Class """
import json
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestFileStorageInit(unittest.TestCase):
    """Testing basic instantiation and private class attributes"""


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

    """def test_save_and_relod(self):
    Testing save() and reload() methods
        self.storage.save()
        new = FileStorage()
        new.reload()
        self.assertIn(self.obj_1, new.all().keys())
        self.assertIn(self.obj_2, new.all().keys())"""

    if __name__ == "__main__":
        unittest.main()
