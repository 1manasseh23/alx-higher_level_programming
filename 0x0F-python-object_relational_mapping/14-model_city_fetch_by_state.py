#!/usr/bin/python3
"""
This a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.

City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string
of 128 characters and can’t be null
class attribute state_id that represents a column of an integer,
can’t be null and is a foreign key to states.id
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username,
                password,
                db_name),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(
            City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
