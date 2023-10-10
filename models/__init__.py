#!/usr/bin/python3
"""File storage __init__ method"""
from models.engine.file_storage import FileStorage


# instance of FileStorage
storage = FileStorage()  # creates new FileStorage instance
storage.reload()  # loads objects from the json file
