#!/usr/bin/python3
"""
file_storage module : contains necessary class and
methods for serialization/deserialization
"""
import json
import os
from models.base_model import *

class FileStorage:
    """
    FileStorage class
    a class responsible for serialization/deserialization
    """
    def __init__(self) -> None:
        self.__file_path:str = "file.json"
        self.__objects:dict = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()
        return
    
    def save(self):
        with open(self.__file_path, "w") as fp:
            json.dump(self.__objects, fp)
        return
    
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as fp:
                for key in self.__objects:
                    self.__objects[key] = BaseModel(**self.__objects[key])
        else:
            pass
        return
