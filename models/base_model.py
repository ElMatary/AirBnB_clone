#!/usr/bin/python3
"""defines all common attributes and methods"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:

    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "updated_at" or k == "created_at":
                        self.__dict__[k] = datetime.fromisoformat(v)
                    else:
                        self.__dict__[k] = v

    def __str__(self):
        """return str"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Update with the current date and time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys and values"""

        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = self.__class__.__name__
        my_dictionary["updated_at"] = self.updated_at.isoformat()
        my_dictionary["created_at"] = self.created_at.isoformat()
        return my_dictionary
