#!/usr/bin/python3
"""
This a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> \
                        <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create an engine to connect to the MySQL server
    lst = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    username, password, db_name, search_name = lst
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the State object with the specified name
    state = session.query(State).filter_by(name=search_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
