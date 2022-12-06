#!/usr/bin/python3

""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to execute quries with SQL
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
