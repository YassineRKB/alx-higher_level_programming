#!/usr/bin/python3
"""script to list all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cursor = db.cursor()
    querry = "SELECT * FROM states WHERE name LIKE '{}' \
ORDER BY id ASC".format(argv[4])
    cursor.execute(querry)
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
