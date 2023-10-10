#!/usr/bin/python3
""" This Module contains UnitTests for the Amenity Class """
import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestAmenityAttributes(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.a1 = Amenity()
        self.a2 = Amenity()

    def tearDown(self):
        del self.a1
        del self.a2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.a1.name, "")
        self.a1.name = "Testor"
        self.assertEqual(self.a1.name, "Testor")


class TestBaseModelInit(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.a1 = Amenity()
        self.a2 = Amenity()

    def tearDown(self):
        del self.a1
        del self.a2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.a1.created_at, self.a1.updated_at)
        self.assertEqual(self.a2.created_at, self.a2.updated_at)
        self.assertNotEqual(self.a1.created_at, self.a2.created_at)
        self.assertNotEqual(self.a1.updated_at, self.a2.updated_at)
        self.assertNotEqual(self.a1.id, self.a2.id)
        self.assertEqual(len(self.a1.id), 36)
        self.assertTrue(type(self.a1.id), str)
        self.assertTrue(type(self.a1.created_at), str)
        self.assertTrue(type(self.a1.updated_at), str)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.a1), f"{self.a1}")
        self.assertEqual(self.a1.__str__(), f"{self.a1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.a1.save()
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)
        self.assertTrue(self.a1.created_at < self.a1.updated_at)
        with self.assertRaises(TypeError):
            self.a1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        a1_dict = self.a1.to_dict()
        self.assertTrue(type(a1_dict), dict)
        self.assertEqual(a1_dict["__class__"], self.a1.__class__.__name__)
        self.assertEqual(a1_dict["created_at"], self.a1.created_at.isoformat())
        self.assertEqual(a1_dict["updated_at"], self.a1.updated_at.isoformat())
        self.assertEqual(a1_dict["id"], self.a1.id)
        with self.assertRaises(TypeError):
            self.a1.to_dict(1)
