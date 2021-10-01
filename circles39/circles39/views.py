
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def reg(request):
    return render(request, 'reg.html')

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
    return render(request, 'account.html')