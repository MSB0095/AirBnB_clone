#!/usr/bin/python3
"""
base_model - module
provides a base class model for use in the project
"""
import uuid
import datetime


class BaseModel:
    """
    BaseModel class
    provides a base class model
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        init method
        it runs at the creation of each instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.key = datetime.datetime.fromisoformat(value)
                else:
                    self.key = value
        return

    def __str__(self) -> str:
        """
        str method
        returns a str of the instance
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self) -> None:
        """
        save method - updates the updated_at date
        """
        self.updated_at = datetime.datetime.now()
        return

    def to_dict(self) -> dict:
        """
        to_dict method - returns a dictionnary of the object
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
