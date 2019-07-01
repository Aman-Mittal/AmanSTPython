import sqlite3 as lite
con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute('''CREATE TABLE Cars(
        id Int,Name TEXT,Price INT)''')
    print("table cars created")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',5712)")
print("Values in table Cars inserted")
