#!/usr/bin/python3
'''State and base classes - instance of declarative_base()'''
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


ourMetaData = MetaData()
Base = declarative_base(metadata=ourMetaData)


class State(Base):
    '''Class with id and name attributes '''
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
