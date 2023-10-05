#!/usr/bin/python3
""" This Module contains UnitTests for the BaseModel Class """
import unittest
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """ This Test Class tests the BaseModel constructor """

    def test_base_model_constructor(self):
        """ Testing Constructor """
        b1 = BaseModel()
        self.assertNotEqual(b1.created_at, b1.updated_at)
        self.assertEqual(len(b1.id), 36)
        with self.assertRaises(TypeError):
            BaseModel(1)

    def test_save_method(self):
        """ Testing Save Method """
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)
        with self.assertRaises(TypeError):
            b1 = BaseModel()
            b1.save(1)

    def test_to_dict_method(self):
        """ Testing to_dict Method """
        with self.assertRaises(TypeError):
            b1 = BaseModel()
            b1.to_dict(1)
