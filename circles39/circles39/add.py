import sqlite3
def add(name, type, age, price, pfdo, geo):
    try:
        with open('2.txt', 'r') as f:
            c = f.read()
        cc = c
        con = sqlite3.connect('mydatabase2.db')
        cur = con.cursor()
        a = [c, name, type, age, price, pfdo, geo]
        cur.execute('INSERT INTO cources VALUES (?, ?, ?, ?, ?, ?, ?)', a)
        con.commit()
    except Exception as e:
        print(e)
    with open('2.txt', 'w') as f:
        xd = str(int(cc)+1)
        f.write(xd)
