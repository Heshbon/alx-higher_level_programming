#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print("Fail to connect to the database")
        exit(1)

    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id ASC;")

    result = c.fetchall()

    for line in result:
        print(line)

    c.close()
    db.close()
