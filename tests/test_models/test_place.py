#!/usr/bin/python3
""" This Module contains UnitTests for the Place Class """
import unittest
import models
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestPlaceAttributes(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.p1 = Place()
        self.p2 = Place()

    def tearDown(self):
        del self.p1
        del self.p2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.p1.city_id, "")
        self.assertEqual(self.p1.user_id, "")
        self.assertEqual(self.p1.name, "")
        self.assertEqual(self.p1.description, "")
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertEqual(self.p1.max_guest, 0)
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertEqual(self.p1.latitude, 0.0)
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertEqual(self.p1.amenity_ids, [])
        self.p1.city_id = "test"
        self.p1.user_id = "test"
        self.p1.name = "Tester"
        self.p1.description = "test"
        self.p1.number_rooms = 1
        self.p1.number_bathrooms = 1
        self.p1.max_guest = 1
        self.p1.price_by_night = 1
        self.p1.latitude = 1.0
        self.p1.longitude = 1.0
        self.p1.amenity_ids = ["test"]
        self.assertEqual(self.p1.city_id, "test")
        self.assertEqual(self.p1.user_id, "test")
        self.assertEqual(self.p1.name, "Tester")
        self.assertEqual(self.p1.description, "test")
        self.assertEqual(self.p1.number_rooms, 1)
        self.assertEqual(self.p1.number_bathrooms, 1)
        self.assertEqual(self.p1.max_guest, 1)
        self.assertEqual(self.p1.price_by_night, 1)
        self.assertEqual(self.p1.latitude, 1.0)
        self.assertEqual(self.p1.longitude, 1.0)
        self.assertEqual(self.p1.amenity_ids, ["test"])


class TestBaseModelInit(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.p1 = Place()
        self.p2 = Place()

    def tearDown(self):
        del self.p1
        del self.p2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.p1.created_at, self.p1.updated_at)
        self.assertEqual(self.p2.created_at, self.p2.updated_at)
        self.assertNotEqual(self.p1.created_at, self.p2.created_at)
        self.assertNotEqual(self.p1.updated_at, self.p2.updated_at)
        self.assertNotEqual(self.p1.id, self.p2.id)
        self.assertEqual(len(self.p1.id), 36)
        self.assertTrue(type(self.p1.id), str)
        self.assertTrue(type(self.p1.created_at), str)
        self.assertTrue(type(self.p1.updated_at), str)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.p1), f"{self.p1}")
        self.assertEqual(self.p1.__str__(), f"{self.p1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.p1.save()
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)
        self.assertTrue(self.p1.created_at < self.p1.updated_at)
        with self.assertRaises(TypeError):
            self.p1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        p1_dict = self.p1.to_dict()
        self.assertTrue(type(p1_dict), dict)
        self.assertEqual(p1_dict["__class__"], self.p1.__class__.__name__)
        self.assertEqual(p1_dict["created_at"], self.p1.created_at.isoformat())
        self.assertEqual(p1_dict["updated_at"], self.p1.updated_at.isoformat())
        self.assertEqual(p1_dict["id"], self.p1.id)
        with self.assertRaises(TypeError):
            self.p1.to_dict(1)
