#!/usr/bin/python3

from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City

def fetch_cities_by_state(username, password, db_name):
    # Create a database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Bind the engine to the Base
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all City objects and sort by id
        cities = session.query(City).order_by(City.id).all()

        # Print results in the specified format
        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, db_name)