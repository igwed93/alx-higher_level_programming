#!/usr/bin/python3
"""returns the first state object from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # query python instances in database
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{:d}: {:s}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
