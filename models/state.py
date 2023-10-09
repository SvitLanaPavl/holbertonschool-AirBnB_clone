#!/usr/bin/python3
""" This module contains the definition for the 'State' Class """
import base_model


class State(base_model.BaseModel):
    """ Class Definition for State Class, Subclass of BaseModel """

    def __init__(self, name=""):
        super().__init__()
        self.name = name

