#!/usr/bin/python3
"""State model with a relationship to City objects."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base


class State(Base):
    """Represents a state in the states table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan"
    )
