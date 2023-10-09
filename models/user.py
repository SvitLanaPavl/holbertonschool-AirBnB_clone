#!/usr/bin/python3
""" This module contains the definition for the 'User' Class """
import base_model


class User(base_model.BaseModel):
    """ Class Definition for User Class, Subclass of BaseModel """

    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
