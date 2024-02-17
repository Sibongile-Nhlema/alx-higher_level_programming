#!/usr/bin/python3
'''
prints State object with name
passed as argument from db
'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_pwd = sys.argv[2]
    db_name = sys.argv[3]

    eng = create_engine('mysql+mysqldb://{user}:{pwd}@localhost:3306/{db_name}'
                        .format(user=db_user, pwd=db_pwd, db_name=db_name))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()

    try:
        for state in session.query(State).order_by(State.id):
            for city in state.cities:
                print(city.id, city.name, sep=": ", end="")
                print(" -> " + state.name)
