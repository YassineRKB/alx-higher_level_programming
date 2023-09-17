#!/usr/bin/python3
"""script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa"""
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    conString = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conString)
    Base.metadata.create_all(engine)
    SessObj = sessionmaker(bind=engine)
    session = SessObj()
    data = session.query(State).order_by(State.id).all()
    for row in data:
        print(f"{row.id}: {row.name}")
        for city in row.cities:
            print(f"    {city.id}: {city.name}")
    session.close()