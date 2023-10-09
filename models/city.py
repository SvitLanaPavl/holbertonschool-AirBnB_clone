#!/usr/bin/python3
""" This module contains the definition for the 'City' Class """
import base_model


class City(base_model.BaseModel):
    """ Class Definition for City Class, Subclass of BaseModel """

    def __init__(self, state_id="", name=""):
        super().__init__()
        self.state_id = state_id
        self.name = name

