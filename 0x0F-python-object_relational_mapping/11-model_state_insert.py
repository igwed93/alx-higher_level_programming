#!/usr/bin/python3

"""
adds the State object 'Louisiana' to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # create engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # add new_state to the database & commit changes
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print('{:d}'.format(new_state.id))

    session.close()
