#!/usr/bin/python3
""" This module contains the definition for the 'Amenity' Class """
import base_model


class Amenity(base_model.BaseModel):
    """ Class Definition for Amenity Class, Subclass of BaseModel """

    def __init__(self, name=""):
        super().__init__()
        self.name = name
