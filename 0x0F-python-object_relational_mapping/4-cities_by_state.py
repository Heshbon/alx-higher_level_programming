#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    if (len(argv) != 4):
        print('Usage: username, password, database name')
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Fail to connect to the database')
        exit(1)

    c = db.cursor()

    c.execute("""SELECT city.id, city.name, state.name FROM cities as city
                      INNER JOIN states as state
                      ON city.state_id = state.id
                      ORDER BY city.id ASC;""")

    sql_query = c.fetchall()

    for line in sql_query:
        print(line)

    c.close()
    db.close()
