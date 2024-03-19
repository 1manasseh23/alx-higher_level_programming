#!/usr/bin/python3
"""
This a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, db_name):
    # Create a database connection
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
            )

    # Bind the engine to the Base
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query and delete State objects with 'a' in their name
        states_to_delete = session.query(State).filter(
                State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)

        # Commit the changes
        session.commit()
        print("States with 'a' in their name \
                have been deleted successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> \
                <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_states_with_a(username, password, db_name)
