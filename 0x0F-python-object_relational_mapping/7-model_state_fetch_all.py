#!/usr/bin/python3
"""
A python script that lists all 'State' objects from the
database 'hbtn_0e_6_usa'
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    pswd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, pswd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
