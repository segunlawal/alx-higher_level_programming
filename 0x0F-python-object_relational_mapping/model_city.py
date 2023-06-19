#!/usr/bin/python3
"""contains the class definition of a City and an instance Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
                Integer,
                nullable=False,
                ForeignKey("states.id"))
