#!/usr/bin/python3
"""Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
(Safe from SQL Injection)"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql
    import re

    # Code not executed when imported
    if (len(argv) != 5):
        print('Usage: username, password, database name, state name')
        exit(1)

    searched = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('A valid state name')
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Fail to connect to the database')
        exit(1)

    c = db.cursor()

    c.execute("SELECT * FROM states \
                    WHERE name = '{:s}' ORDER BY states.id ASC;".format(searched))

    sql_query = c.fetchall()

    for line in sql_query:
        print(line)

    c.close()
    db.close()
