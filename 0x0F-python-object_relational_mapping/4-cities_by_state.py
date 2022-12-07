#!/usr/bin/python3

""" module that lists all cities from database hbtn_0e_4_usa """

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
    sql_cmd = "SELECT cities.id, states.name, cities.name \
               FROM cities \
               INNER JOIN states ON cities.state_id = states.id"
    c.execute(sql_cmd)
    for city in c.fetchall():
        print(city)
    c.close()
    db.close()
