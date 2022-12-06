#!/usr/bin/python3

"""
script that lists all states that starts with N
from the database hbtn_0e_0_usa
"""

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
    cursor = db.cursor()
    sql_cmd = """SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (argv[4], ))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
