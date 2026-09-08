#!/usr/bin/python3
"""
Script isoma no kwereka ama state hamwe n'imijyi iyishamikiyeho
uhereye kuri database hbtn_0e_4_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda x: x.id):
            print("    {}: {}".format(city.id, city.name))

    session.close()
zd
