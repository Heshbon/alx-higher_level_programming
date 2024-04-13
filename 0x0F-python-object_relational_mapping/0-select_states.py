#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print("Usage: <mysql username> <mysql password> <database name>")
        exit(0)

    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY states.id;")

    result = c.fetchall()

    for row in result:
        print(row)

    c.close()
    db.close()
