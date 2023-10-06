#!/usr/bin/python3
""" This Module contains UnitTests for the BaseModel Class """
import unittest
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """ This Test Class tests the BaseModel constructor """

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        del self.b1
        del self.b2

    def test_base_model_constructor(self):
        """ Testing Constructor """
        self.assertEqual(self.b1.created_at, self.b1.updated_at)
        self.assertEqual(self.b2.created_at, self.b2.updated_at)
        self.assertNotEqual(self.b1.created_at, self.b2.created_at)
        self.assertNotEqual(self.b1.updated_at, self.b2.updated_at)
        self.assertEqual(len(self.b1.id), 36)
        self.assertTrue(type(self.b1.id), str)
        self.assertTrue(type(self.b1.created_at), str)
        self.assertTrue(type(self.b1.updated_at), str)
        with self.assertRaises(TypeError):
            BaseModel(1)

    def test_str_override(self):
        """ Testing __str__ override """
        self.assertEqual(str(self.b1), f"{self.b1}")
        self.assertEqual(self.b1.__str__(), f"{self.b1}")

    def test_save_method(self):
        """ Testing Save Method """
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)
        self.assertTrue(self.b1.created_at < self.b1.updated_at)
        with self.assertRaises(TypeError):
            self.b1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        b1_dict = self.b1.to_dict()
        self.assertTrue(type(b1_dict), dict)
        self.assertEqual(b1_dict["__class__"], self.b1.__class__.__name__)
        self.assertEqual(b1_dict["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(b1_dict["updated_at"], self.b1.updated_at.isoformat())
        self.assertEqual(b1_dict["id"], self.b1.id)
        with self.assertRaises(TypeError):
            self.b1.to_dict(1)
