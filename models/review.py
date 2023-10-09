#!/usr/bin/python3
""" This module contains the definition for the 'Review' Class """
import base_model


class Review(base_model.BaseModel):
    """ Class Definition for Review Class, Subclass of BaseModel """

    place_id = ""
    user_id = ""
    text = ""
