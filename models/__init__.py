#!/usr/bin/python3
"""File storage instance module"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# instance of FileStorage
storage = FileStorage()
storage.reload()
