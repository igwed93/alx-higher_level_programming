#!/usr/bin/python3

"""
searches for a state and prints its id
from the database hbtn_0e_6_usa
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
    state = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cond = False

    # query python instances in database that contain the letter 'a'
    for obj in session.query(State).order_by(State.id):
        if obj.name == state:
            print('{:d}'.format(obj.id))
            cond = True
    if not cond:
        print('Not found')
