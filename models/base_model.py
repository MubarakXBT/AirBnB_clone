#!/usr/bin/python3
"""
Console Module
uuid
datetime
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A Console Module Basemodel
    """
    def __init__(self, *args, **kwargs):
        """
        instanation of the public instance attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Format how instance object print
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """
        used to update time of last update
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        return dictionar key/value of __dict__ of the Models instance
        """

        result_dict = self.__dict__.copy()
        if (type(self.created_at) == str):
            result_dict["created_at"] = self.created_at
        else:
            result_dict["created_at"] = self.created_at.isoformat()

        if (type(self.created_at) == str):
            result_dict["updated_at"] = self.updated_at
        else:
            result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict
