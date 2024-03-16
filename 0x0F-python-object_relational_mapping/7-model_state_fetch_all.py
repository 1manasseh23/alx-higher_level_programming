#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    try:
        # Connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all State objects and display results
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)
