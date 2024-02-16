#!/usr/bin/python3
'''
script that takes in the name of a state as an argument and
lists all cities of that state
using the database hbtn_0e_4_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":
    '''Connect to the MySQL server'''
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    state = sys.argv[4]
    query = "SELECT cities.name FROM cities \
            INNER JOIN states ON states.id=cities.state_id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC"

    cur.execute(query, (state,))
    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    print(*cities, sep=", ")

    cur.close()
    db.close()
