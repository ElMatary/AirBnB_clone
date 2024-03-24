#!/usr/bin/python3
""" File storage """
import json

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place

class FileStorage:
    """serializes and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}
    new_dict = {"User": User, "BaseModel": BaseModel, "City": City,
                "State": State, "Amenity": Amenity, "Review": Review,
                "Place": Place}
    def all(self):
        """returns the dict"""

        return self.__objects
    def new(self, obj):
        '''create new object'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes objects"""
            
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            object_dict = {}
            for key, obj in self.__objects.items():
                object_dict[key] = obj.to_dict()
            json.dump(object_dict, f)
    def reload(self):
        """deserializes the Json file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                object_dict = json.load(f)
            for key, value in object_dict.items():
                clss_nme = value.get('__class__')
                obj_class = self.new_dict.get(clss_nme)
                if obj_class:
                    obj = obj_class(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
