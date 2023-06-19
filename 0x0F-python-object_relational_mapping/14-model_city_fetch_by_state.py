#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access database and list the cities from the database
    """

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(
        State.name, City.id, City.name).join(State).order_by(City.id)
    for item in query:
        print(f"{item[0]}: ({item[1]}) {item[2]}")

    session.commit()
    session.close()
