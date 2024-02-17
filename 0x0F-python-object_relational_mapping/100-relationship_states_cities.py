#!/usr/bin/python3
''' prints the State object with the name passed as argument from the database
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

    for i in session.query(State).order_by(State.id):
        print(i.id, i.name, sep=": ")
        for city_ins in i.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
