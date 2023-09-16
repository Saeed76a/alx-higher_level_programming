#!/usr/bin/python3
"""Filter states"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()

    cur.execute("SELECT name, id FROM states WHERE name LIKE 'N%';")
    all_rows = cur.fetchall()

    for one in all_rows:
        print(one)
