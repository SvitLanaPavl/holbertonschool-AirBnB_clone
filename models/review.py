#!/usr/bin/python3
""" This module contains the definition for the 'Review' Class """
import base_model


class Review(base_model.BaseModel):
    """ Class Definition for Review Class, Subclass of BaseModel """

    def __init__(self, place_id="", user_id="", text=""):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
