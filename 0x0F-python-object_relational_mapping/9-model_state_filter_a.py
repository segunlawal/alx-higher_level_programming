#!/usr/bin/python3
"""script lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access database and list the states from the database
    """

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).order_by(State.id)
    letter = 'a'
    for state in query:
        if letter.lower() in state.lower():
            print(f"{state.id}: {state.name}")
    session.commit()
    session.close()
    engine.dispose()
