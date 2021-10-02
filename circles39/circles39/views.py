from . import main
import sqlite3
from . import add_circle
import os
from django.shortcuts import render
from . import si_child
from . import si_parent
from . import login_func

def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')

def add_post(request):
    org = request.POST.get("org")
    type = request.POST.get("type")
    mn_age = request.POST.get("mn_age")
    mx_age = request.POST.get("mx_age")
    mn_money = request.POST.get("mn_money")
    mx_money = request.POST.get("mx_money")
    check = request.POST.get("chck")
    lok = request.POST.get("lok")
    age = (int(mn_age) + int(mx_age)) / 2
    money = (int(mn_money) + int(mx_money)) / 2

    add_circle.add(org, type, age, money, check, lok)

    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signup_child(request):
    return render(request, 'signup_child.html')

def signup_parent(request):
    return render(request, 'signup_parent.html')

def login(request):
    return render(request, 'login.html')

def testfilter(request):
    return render(request, 'testfilter.html')

def test(request):
    return render(request, 'test.html')

def filter(request):
    return render(request, 'filter.html')

def liked(request):
    return render(request, 'liked.html')

def contacts(request):
    return render(request, 'contacts.html')

def account(request):
    c = False
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'circles39/3.txt'), 'r') as f:
        main.signuped = f.read()
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()
    r = cur.fetchall()
    cur.execute('SELECT * FROM accounts WHERE login = ?', [main.signuped])
    if len(r)!=0:
        c = bool(r[0][7])
        print(c)
        print(r)

    ctx = {
        'signuped': main.signuped,
        'boolean': c
    }

    return render(request, 'account.html', ctx)

def log_in(request):
    login = request.POST.get("login")
    password = request.POST.get("password")

    if login_func.lgn(login, password) == 'xd':
        return render(request, 'index.html')
    main.acnt(login)

    return render(request, 'index.html')

def logout(request):
    main.acnt('-')
    return render(request, 'index.html')

def sign_up_parent(request):
    login = request.POST.get("login")
    password = request.POST.get("password")
    mail = request.POST.get("mail")
    kod = request.POST.get("kod")
    nomer = request.POST.get("nomer")

    si_parent.register(login, password, mail, kod, nomer, 1)
    main.acnt(login)

    return render(request, 'index.html')

def sign_up_child(request):
    login = request.POST.get("login")
    password = request.POST.get("password")
    nomer = request.POST.get("mail")
    main.check()
    acc = main.signuped
    si_child.reg_chld(login, password, nomer, acc, 0)

    return render(request, 'index.html')
