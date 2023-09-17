#!/usr/bin/python3
"""script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa"""
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    conString = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conString)
    SessObj = sessionmaker(bind=engine)
    session = SessObj()
    stateObj = State(name="California")
    session.add(stateObj)
    city = City(name="San Francisco", state=stateObj)
    session.add(city)
    session.commit()
    session.close()
