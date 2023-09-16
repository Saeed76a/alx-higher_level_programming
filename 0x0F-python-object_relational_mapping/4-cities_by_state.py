#!/usr/bin/python3
"""all cities"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    Mydb = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = Mydb.cursor()

    cur.execute('SELECT * FROM cities ORDER BY id ASC')
    all = cur.fetchall()

    for one in all:
        print(one)
