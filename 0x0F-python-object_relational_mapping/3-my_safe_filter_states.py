#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
but safe from MySQL injections!"""

import MySQLdb
from sys import argv

# Code not executed when imported
if __name__ == '__main__':

    # Creates a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    line = c.fetchall()
    for a in line:
        print(a)

    c.close()
    db.close()
