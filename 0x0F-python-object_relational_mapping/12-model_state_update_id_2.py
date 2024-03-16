#!/usr/bin/python3

# 12-model_state_update_id_2.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create an engine to connect to the MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, db_name))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the State object with ID 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with ID 2 not found.")

    # Fetch and print the updated list of states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
