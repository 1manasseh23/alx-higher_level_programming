#!/usr/bin/python3
"""
This a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> \
                <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create an engine to connect to the MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name))

    # Create the State object for Louisiana
    new_state = State(name="Louisiana")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the new state to the database
    session.add(new_state)
    session.commit()

    print(new_state.id)
