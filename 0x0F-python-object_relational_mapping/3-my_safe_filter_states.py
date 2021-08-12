#!/usr/bin/python3
"""
A python script that that takes in arguments and displays all values
in the 'states' table of 'hbtn_0e_0_usa' where name matches the argument.
Safe from MySQL injections!
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cmd = """SELECT *
             FROM states
             WHERE name=%s ORDER BY id ASC"""
    cursor.execute(cmd, (argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
