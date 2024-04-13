#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
from the database"""

import MySQLdb
from sys import argv

# Code not executed when imported
if __name__ == '__main__':
    # creates a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = c.fetchall()
    for a in rows:
        print(a)

    c.close()
    db.close()
