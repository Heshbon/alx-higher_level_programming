#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

# Code not executed when imported
if __name__ == '__main__':

    # Creates a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC".format(argv[4])
    c.execute(sql_query)

    line = c.fetchall()
    for a in line:
        print(a)

    c.close()
    db.close()
