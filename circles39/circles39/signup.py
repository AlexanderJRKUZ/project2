import sqlite3
def register(login, password, mail, number, data):
    with open('1.txt', 'r') as f:
        c = f.readline()
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    cur.execute('''SELECT * FROM accounts WHERE login = ?''', [login])
    r = cur.fetchall()
    if len(r) != 0 and r[0][1] == login:
        print('Аккаунт с таким логином уже существует') # заменить на норм
    else:
        a = [c, login, password, mail, number, data, '-']
        cur.execute("""INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?)""", a)
        con.commit()

        with open('1.txt', 'w') as f:
            xd = str(int(c)+1)
            f.write(xd)
    

