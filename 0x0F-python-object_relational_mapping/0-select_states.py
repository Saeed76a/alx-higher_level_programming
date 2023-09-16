#!/usr/bin/python3
"""Get all states and display them."""


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

    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    all_rows = cur.fetchall()

    for one in all_rows:
        print(one)

    cur.close()
    db.close()
