#!/usr/bin/python3
"""script to add the State object “Louisiana” to the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    conString = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conString)
    SessObj = sessionmaker(bind=engine)
    session = SessObj()
    newStateObject = State(name="Louisiana")
    session.add(newStateObject)
    session.commit()
    print(newStateObject.id)
    session.close()
