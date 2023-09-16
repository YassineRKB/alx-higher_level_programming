#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using
the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cursor = db.cursor()
    querry = "SELECT cities.name FROM states \
    JOIN cities ON states.id = cities.state_id \
    WHERE state.name = %s \
    ORDER BY cities.id"
    cursor.execute(querry, (argv[4],))
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
