import sqlite3
con=sqlite3.connect('test.db')
cur=con.cursor()
cur.execute('SELECT SQLITE_VERSION()')

data=cur.fetchone()
print('\n SQLite Version',data)
