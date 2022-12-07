#!/usr/bin/python3

"""
module that takes a state from user and lists all
cities from database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # create a connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # create cursor to execute queries using SQL
    c = db.cursor()
    sql_cmd = "SELECT cities.name \
               FROM states \
               INNER JOIN cities ON states.id = cities.state_id \
               WHERE states.name LIKE %s \
               ORDER BY cities.id ASC"

    c.execute(sql_cmd, (argv[4],))

    # format the printing of cities of same state separated by commas
    print(', '.join(["{:s}".format(city[0]) for city in c.fetchall()]))

    c.close()
    db.close()
