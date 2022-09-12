#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """Amenities class"""
    if TYPE_STORAGE == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:                   
        name = ""
