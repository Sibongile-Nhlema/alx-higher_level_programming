#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys

if __name__ == "__main__":
    '''Connect to the MySQL server'''
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    '''Execute the SQL query to retrive the states'''
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY state.id ASC")
    rows = cur.fetchall()

    '''Show results'''
    for row in rows:
        print(row)

    cur.close()
    db.close()
