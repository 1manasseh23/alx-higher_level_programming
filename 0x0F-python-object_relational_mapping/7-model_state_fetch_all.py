#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Create an engine to connect to the MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all State objects sorted by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")
