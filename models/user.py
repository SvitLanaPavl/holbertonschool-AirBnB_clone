#!/usr/bin/python3
""" This module contains the definition for the 'User' Class """
import base_model


class User(base_model.BaseModel):
    """ Class Definition for User Class, Subclass of BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
