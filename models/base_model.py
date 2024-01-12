#!/usr/bin/python3
"""
Console Module
uuid
datetime
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A Console Module Basemodel
    """
    def __init__(self):
        """
        instanation of the public instance attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Format how instance object print
        """
        prnt = "["+__class__.__name__+"] ("\
            +str(self.id)+") "+str(self.__dict__)
        return (prnt)

    def save(self):
        """
        used to update time of last update
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return dictionar key/value of __dict__ of the instance
        """

        return {"my_number": self.my_number,
                "name": self.name,
                "__class__": __class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                }
