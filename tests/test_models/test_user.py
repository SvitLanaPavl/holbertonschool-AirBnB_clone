#!/usr/bin/python3
""" This Module contains UnitTests for the User Class """
import unittest
import models
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestUserAttributes(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.u1 = User()
        self.u2 = User()

    def tearDown(self):
        del self.u1
        del self.u2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.u1.email, "")
        self.assertEqual(self.u1.password, "")
        self.assertEqual(self.u1.first_name, "")
        self.assertEqual(self.u1.last_name, "")
        self.u1.email = "test@email.com"
        self.u1.password = "test"
        self.u1.first_name = "Tester"
        self.u1.last_name = "McTesterson"
        self.assertEqual(self.u1.email, "test@email.com")
        self.assertEqual(self.u1.password, "test")
        self.assertEqual(self.u1.first_name, "Tester")
        self.assertEqual(self.u1.last_name, "McTesterson")


class TestBaseModelInit(unittest.TestCase):
    """Testing basic instantiation and attribute assignment """

    def setUp(self):
        self.u1 = User()
        self.u2 = User()

    def tearDown(self):
        del self.u1
        del self.u2

    def test_standard_use(self):
        """ Basic Instantiation """
        self.assertEqual(self.u1.created_at, self.u1.updated_at)
        self.assertEqual(self.u2.created_at, self.u2.updated_at)
        self.assertNotEqual(self.u1.created_at, self.u2.created_at)
        self.assertNotEqual(self.u1.updated_at, self.u2.updated_at)
        self.assertNotEqual(self.u1.id, self.u2.id)
        self.assertEqual(len(self.u1.id), 36)
        self.assertTrue(type(self.u1.id), str)
        self.assertTrue(type(self.u1.created_at), str)
        self.assertTrue(type(self.u1.updated_at), str)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.u1), f"{self.u1}")
        self.assertEqual(self.u1.__str__(), f"{self.u1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.u1.save()
        self.assertNotEqual(self.u1.created_at, self.u1.updated_at)
        self.assertTrue(self.u1.created_at < self.u1.updated_at)
        with self.assertRaises(TypeError):
            self.u1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        u1_dict = self.u1.to_dict()
        self.assertTrue(type(u1_dict), dict)
        self.assertEqual(u1_dict["__class__"], self.u1.__class__.__name__)
        self.assertEqual(u1_dict["created_at"], self.u1.created_at.isoformat())
        self.assertEqual(u1_dict["updated_at"], self.u1.updated_at.isoformat())
        self.assertEqual(u1_dict["id"], self.u1.id)
        with self.assertRaises(TypeError):
            self.u1.to_dict(1)
