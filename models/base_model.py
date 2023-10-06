#!/usr/bin/python3
"""The BaseModel Module"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class documentation"""

    def __init__(self, *args, **kwargs):
        """The constructor method
        
        Arguments:
        *args: not used
        **kwargs: dictionary representation
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created at", "updated at"]:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing ke/values of __dict__"""
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = dict_repr["created_at"].isoformat()
        dict_repr["updated_at"] = dict_repr["updated_at"].isoformat()
        return dict_repr
