#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    State class definition.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

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
        print("Table 'states' created successfully!")

    except Exception as e:
        print("Error creating table: {}".format(e))
        sys.exit(1)
