#!/usr/bin/python3
"""
A python script that prints all 'City' objects from the
database 'hbtn_0e_14_usa'
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    pswd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, pswd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(state[0], state[1], state[2]))

    session.close()
