#!/usr/bin/python3
""" This Module contains UnitTests for the Review Class """
import unittest
import models
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestReviewAttributes(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.r1 = Review()
        self.r2 = Review()

    def tearDown(self):
        del self.r1
        del self.r2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.r1.place_id, "")
        self.assertEqual(self.r1.user_id, "")
        self.assertEqual(self.r1.text, "")
        self.r1.place_id = "test"
        self.r1.user_id = "test"
        self.r1.text = "Tester"
        self.assertEqual(self.r1.place_id, "test")
        self.assertEqual(self.r1.user_id, "test")
        self.assertEqual(self.r1.text, "Tester")


class TestBaseModelInit(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.r1 = Review()
        self.r2 = Review()

    def tearDown(self):
        del self.r1
        del self.r2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.r1.created_at, self.r1.updated_at)
        self.assertEqual(self.r2.created_at, self.r2.updated_at)
        self.assertNotEqual(self.r1.created_at, self.r2.created_at)
        self.assertNotEqual(self.r1.updated_at, self.r2.updated_at)
        self.assertNotEqual(self.r1.id, self.r2.id)
        self.assertEqual(len(self.r1.id), 36)
        self.assertTrue(type(self.r1.id), str)
        self.assertTrue(type(self.r1.created_at), str)
        self.assertTrue(type(self.r1.updated_at), str)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.r1), f"{self.r1}")
        self.assertEqual(self.r1.__str__(), f"{self.r1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.r1.save()
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)
        self.assertTrue(self.r1.created_at < self.r1.updated_at)
        with self.assertRaises(TypeError):
            self.r1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        r1_dict = self.r1.to_dict()
        self.assertTrue(type(r1_dict), dict)
        self.assertEqual(r1_dict["__class__"], self.r1.__class__.__name__)
        self.assertEqual(r1_dict["created_at"], self.r1.created_at.isoformat())
        self.assertEqual(r1_dict["updated_at"], self.r1.updated_at.isoformat())
        self.assertEqual(r1_dict["id"], self.r1.id)
        with self.assertRaises(TypeError):
            self.r1.to_dict(1)
