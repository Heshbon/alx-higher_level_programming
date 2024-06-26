#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql
    import re

    if (len(argv) != 5):
        print('Usage: username, password, database name, state name')
        exit(1)

    state_name = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('A valid state name')
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Fail to connect to the database')
        exit(1)

    cursor = db.cursor()

    value = cursor.execute("""SELECT c.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      WHERE s.name = '{:s}'
                      ORDER BY c.id ASC;""".format(state_name))

    result_query = cursor.fetchall()

    last = []

    for a in range(value):
        last.append(result_query[a][0])

    print(', '.join(last))

    cursor.close()
    db.close()
