#!/usr/bin/python3
""" This Module contains UnitTests for the State Class """
import unittest
import models
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestStateAttributes(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.s1 = State()
        self.s2 = State()

    def tearDown(self):
        del self.s1
        del self.s2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.s1.name, "")
        self.s1.name = "Testor"
        self.assertEqual(self.s1.name, "Testor")


class TestBaseModelInit(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.s1 = State()
        self.s2 = State()

    def tearDown(self):
        del self.s1
        del self.s2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.s1.created_at, self.s1.updated_at)
        self.assertEqual(self.s2.created_at, self.s2.updated_at)
        self.assertNotEqual(self.s1.created_at, self.s2.created_at)
        self.assertNotEqual(self.s1.updated_at, self.s2.updated_at)
        self.assertNotEqual(self.s1.id, self.s2.id)
        self.assertEqual(len(self.s1.id), 36)
        self.assertTrue(type(self.s1.id), str)
        self.assertTrue(type(self.s1.created_at), str)
        self.assertTrue(type(self.s1.updated_at), str)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.s1), f"{self.s1}")
        self.assertEqual(self.s1.__str__(), f"{self.s1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.s1.save()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)
        self.assertTrue(self.s1.created_at < self.s1.updated_at)
        with self.assertRaises(TypeError):
            self.s1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        s1_dict = self.s1.to_dict()
        self.assertTrue(type(s1_dict), dict)
        self.assertEqual(s1_dict["__class__"], self.s1.__class__.__name__)
        self.assertEqual(s1_dict["created_at"], self.s1.created_at.isoformat())
        self.assertEqual(s1_dict["updated_at"], self.s1.updated_at.isoformat())
        self.assertEqual(s1_dict["id"], self.s1.id)
        with self.assertRaises(TypeError):
            self.s1.to_dict(1)
