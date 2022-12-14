#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class Place(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """ A place to stay """
    if TYPE_STORAGE == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete")
        place_amenity = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True),
                        Column("amenity_id", String (60), ForeignKey("amenities.id"), primary_key=True),)
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Return a list with the reviews of a place"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """gets a list of amenities linked to the place"""
            list_amenities = []
            for amenity in models.storage.all(Amenity).values(): 
                if amenity.id in self.amenity_ids:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, new_amenity):
            """append new amenities ids to amenity_ids"""
            if type(new_amenity) == Amenity:
                self.amenity_ids.append(new_amenity.id)
