#!/usr/bin/python3
"""This is the file storage module: it creates
a new class"""
import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """Serializes instances to JSON file and
    deserializes JSON file to instances"""

    # path to the JSON file
    __file_path = "file.json"
    # dictionary that maps class names and id's
    __objects = {}

    def all(self):
        """Returns a dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        # collects the serialized data of each object
        dict_obj = FileStorage.__objects
        j_dict_obj = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(j_dict_obj, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                # stores the deserialized JSON data
                dict_obj = json.load(json_file)
                for value in dict_obj.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
