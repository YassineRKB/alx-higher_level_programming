#!/usr/bin/python3
"""script to print all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    conString = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conString)
    SessObj = sessionmaker(bind=engine)
    session = SessObj()
    data = session.query(City, State).join(
        State, State.id == City.state_id
        ).all()
    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
