#!/usr/bin/python3
"""couple cities"""

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

    cur.execute('SELECT cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.state_id ASC')
    all = cur.fetchall()

    string = ''
    for one in all:
        if one[1] == argv[4]:
            string += ', '+one[0]
    print(string[2:])
