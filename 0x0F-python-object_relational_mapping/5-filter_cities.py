#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connects to database
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM cities WHERE BINARY name=%s \
            ORDER BY id", {'name': argv[4]})
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
