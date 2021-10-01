
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