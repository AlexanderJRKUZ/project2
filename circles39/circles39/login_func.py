from django.urls import path
from . import views
import sqlite3
from . import main
account = ''
def lgn(login, password):
    global account
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    a = [login]
    cur.execute('SELECT * FROM accounts WHERE login = ?', a)
    r = cur.fetchall()
    if len(r) != 0 and r[0][1] == login and password == r[0][2]:
        main.acnt(login)
    else:
        path('', views.index, name='home')
        return 'xd'
