#!/usr/bin/python3
"""List cities with their state names."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(
            city.state.name if hasattr(city, "state") else
            session.query(State).filter(State.id == city.state_id).first().name,
            city.id,
            city.name
        ))

    session.close()
