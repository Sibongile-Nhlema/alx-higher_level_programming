#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
Safe from SQL injections
'''
import MySQLdb
import sys

if __name__ == "__main__":
    '''Connect to the MySQL server'''
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    '''Execute the SQL query to retrive the states that match the name gven'''
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    name = (sys.argv[4],)
    cur.execute(query, name)
    rows = cur.fetchall()

    '''Show results'''
    for row in rows:
        print(row)

    cur.close()
    db.close()
