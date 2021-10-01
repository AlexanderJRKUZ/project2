import sqlite3
con = sqlite3.connect("mydatabase.db")

cur = con.cursor()
cur.execute('''CREATE TABLE accounts
(id text, login text, password text, mail text, number text, data text, parent text)''')