import sqlite3
account = ''
def lgn(login, password):
    global account
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    a = [login]
    cur.execute('SELECT * FROM accounts WHERE login = ?', a)
    r = cur.fetchall()
    if len(r) != 0 and r[0][1] == login:
        if r[0][2] == password:
            account = login
    else:
        print('Ошибка')
lg, password = list(map(str, input().split()))
lgn(lg, password)
