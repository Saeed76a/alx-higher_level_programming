#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)
cur = db.cursor()

cur.execute("SELECT id, name FROM states;")
all_rows = cur.fetchall()

for one in all_rows:
    print(one)
