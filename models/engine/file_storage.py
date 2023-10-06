#!/usr/bin/python3
"""File storage module"""
import json


class FileStorage:
    """Serializes instances to JSON file and
    deserializes JSON file to instances"""

    # path to the JSON file
    __file_path = "file.json"
    # dictionary that maps class names and id's
    __objects = {}

    def all(self):
        """Returns a dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        # collects the serialized data of each object
        dict_new = {}
        # each key is unique identifier of an object
        for key in self.__objects:
            # accessing the corresponding object and return dict
            dict_new[key] = self.__objects[key].to_dict()
            # writing the dictionary to json file
        with open(self.__file_path, "w") as json_file:
            json.dump(dict_new, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as json_file:
                # stores the deserialized JSON data
                dict_new = {}
                """reads the contents of the JSON file,
                parses it and loads onto the dict_new"""
                json.loads(json_file.read())
                # each key is a unique identifier for an object
                for key, value in dict_new.items():
                    # check if the key does not exist
                    if key not in self.__objects.keys():
                        # create a new instance of the class
                        class_name = value["__class__"]
                        # create the new instance of the class
                        obj = eval(f"{class_name}(**value)")
                        # adding the object to the dictionary
                        self.new(obj)
        except IOError:
            pass
