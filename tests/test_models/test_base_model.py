#!/usr/bin/python3
""" This Module contains UnitTests for the BaseModel Class """
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


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
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertEqual(len(self.b1.id), 36)
        self.assertTrue(type(self.b1.id), str)
        self.assertTrue(type(self.b1.created_at), str)
        self.assertTrue(type(self.b1.updated_at), str)

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

    def test_new_instance_in_BM(self):
        """testing if new instance is in BaseModel object"""
        new_instance = BaseModel()
        all_obj = models.storage.all().values()
        self.assertIn(new_instance, all_obj)


class TestInstatiationWithKwargs(unittest.TestCase):
    """Testing instantiation with kwargs"""
    def test_kwargs(self):
        """testing kwargs"""
        instance = BaseModel(id="123", created_at="2023-09-28T10:30:00.000000",
                             updated_at="2023-09-28T10:30:00.000000")
        expected_created_at = "2023-09-28T10:30:00"
        expected_updated_at = "2023-09-28T10:30:00"
        self.assertEqual(instance.id, "123")
        self.assertEqual(instance.created_at.isoformat(), expected_created_at)
        self.assertEqual(instance.updated_at.isoformat(), expected_updated_at)

    def test_args(self):
        """test possible args, non datetime arguments"""
        instance_1 = BaseModel(name="Test", number=5)
        self.assertEqual(instance_1.name, "Test")
        self.assertEqual(instance_1.number, 5)

    def test_kwargs_empty(self):
        """test kwargs empty dictionary"""
        instance_2 = BaseModel(**{})
        self.assertEqual(instance_2.created_at, instance_2.updated_at)

    def test_kwargs_None(self):
        """test kwargs None"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
