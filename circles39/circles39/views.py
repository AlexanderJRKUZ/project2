from . import main
from django.shortcuts import render
from . import signup
from . import login_func

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

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
    if main.check():
        main.signuped = True


    ctx = {
        'signuped': main.signuped
    }

    return render(request, 'account.html', ctx)

def sign_up(request):
    login = request.POST.get("login")
    password = request.POST.get("password")
    mail = request.POST.get("mail")
    kod = request.POST.get("kod")
    nomer = request.POST.get("nomer")

    signup.register(login, password, mail, kod, nomer)
    main.acnt(login)

    return render(request, 'index.html')

def log_in(request):
    login = request.POST.get("login")
    password = request.POST.get("password")

    login_func.lgn(login, password)
    main.acnt(login)

    return render(request, 'index.html')

def logout(request):
    main.acnt('-')

    return render(request, 'index.html')
