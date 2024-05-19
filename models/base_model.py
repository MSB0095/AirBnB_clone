import uuid
import datetime


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self) -> None:
        """
        init method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return

    def __str__(self) -> str:
        """
        str method
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
