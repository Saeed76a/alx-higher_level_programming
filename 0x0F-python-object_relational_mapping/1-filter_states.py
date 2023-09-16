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

    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    all_rows = cur.fetchall()

    for one in all_rows:
        if one[1][0] == 'N':
            print(one)
