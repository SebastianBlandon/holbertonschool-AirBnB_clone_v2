#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """ State class """
    if TYPE_STORAGE == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id equals to the current State.id"""
            cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
