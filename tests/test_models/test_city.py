#!/usr/bin/python3
""" This Module contains UnitTests for the City Class """
import unittest
import models
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestCityAttributes(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.c1 = City()
        self.c2 = City()

    def tearDown(self):
        del self.c1
        del self.c2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.c1.state_id, "")
        self.assertEqual(self.c1.name, "")
        self.c1.state_id = "test"
        self.c1.name = "Testor"
        self.assertEqual(self.c1.state_id, "test")
        self.assertEqual(self.c1.name, "Testor")


class TestBaseModelInit(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.c1 = City()
        self.c2 = City()

    def tearDown(self):
        del self.c1
        del self.c2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.c1.created_at, self.c1.updated_at)
        self.assertEqual(self.c2.created_at, self.c2.updated_at)
        self.assertNotEqual(self.c1.created_at, self.c2.created_at)
        self.assertNotEqual(self.c1.updated_at, self.c2.updated_at)
        self.assertNotEqual(self.c1.id, self.c2.id)
        self.assertEqual(len(self.c1.id), 36)
        self.assertTrue(type(self.c1.id), str)
        self.assertTrue(type(self.c1.created_at), str)
        self.assertTrue(type(self.c1.updated_at), str)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.c1), f"{self.c1}")
        self.assertEqual(self.c1.__str__(), f"{self.c1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.c1.save()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)
        self.assertTrue(self.c1.created_at < self.c1.updated_at)
        with self.assertRaises(TypeError):
            self.c1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        c1_dict = self.c1.to_dict()
        self.assertTrue(type(c1_dict), dict)
        self.assertEqual(c1_dict["__class__"], self.c1.__class__.__name__)
        self.assertEqual(c1_dict["created_at"], self.c1.created_at.isoformat())
        self.assertEqual(c1_dict["updated_at"], self.c1.updated_at.isoformat())
        self.assertEqual(c1_dict["id"], self.c1.id)
        with self.assertRaises(TypeError):
            self.c1.to_dict(1)
