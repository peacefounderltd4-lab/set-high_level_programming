#!/usr/bin/python3
"""Define State and its relationship with City."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Represent a state."""

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )
