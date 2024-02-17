#!/usr/bin/python3
''''
Creates the State "California" with
the City "San Francisco" from a database
'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_pwd = sys.argv[2]
    db_name = sys.argv[3]

    eng = create_engine('mysql+mysqldb://{user}:{pwd}@localhost:3306/{db_name}'
                        .format(user=db_user, pwd=db_pwd, db_name=db_name))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()

    new_State = State(name='California')
    new_City = City(name='San Francisco')
    new_State.cities.append(new_City)

    session.add(new_State)
    session.add(new_City)
    session.commit()
