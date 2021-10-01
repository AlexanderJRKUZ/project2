import sqlite3
con = sqlite3.connect("mydatabase2.db")

cur = con.cursor()
cur.execute('''CREATE TABLE cources
(id text, name text, type text, age text, price text, pfdo text, geo text)''')
