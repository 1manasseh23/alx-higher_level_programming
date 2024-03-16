#!/usr/bin/python3

# 9-model_state_filter_a.py

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

    # Fetch all State objects containing the letter "a"
    states_with_a = session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()

    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
