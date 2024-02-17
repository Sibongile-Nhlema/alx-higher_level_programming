#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
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

    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
