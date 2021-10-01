import sqlite3
def register(type, login, password, mail, number, data):
    with open('1.txt', 'r') as f:
        c = f.readline()
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    cur.execute('''SELECT * FROM accounts WHERE login = ?''', [login])
    r = cur.fetchall()
    if len(r) != 0 and r[0][1] == login:
        print('Аккаунт с таким логином уже существует') # заменить на норм
    else:
        if type==1:
            a = [c, login, password, mail, number, data, '-']
            cur.execute("""INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?)""", a)
            con.commit()
        else:
            a = [c, login, password, mail, '-', data, '-']
            cur.execute("""INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?)""", a)
            con.commit()
        with open('1.txt', 'w') as f:
            xd = str(int(c)+1)
            f.write(xd)
    

g = int(input())
if g==1:
    login, password, mail, number, data = list(map(str, input().split()))
    register(1, login, password, mail, number, data)
elif g==0:
    login, password, mail, data = list(map(str, input().split()))
    register(0, login, password, mail, '-', data)