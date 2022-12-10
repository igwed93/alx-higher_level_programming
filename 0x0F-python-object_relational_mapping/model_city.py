#!/usr/bin/python3

"""
This module defines the class City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """ The Class City; instance of Base
        Linked to MySQL table "cities"
    """
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
