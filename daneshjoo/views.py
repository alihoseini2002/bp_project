from django.shortcuts import render
from django.http import HttpResponse

def asli(request):
    a="<a href='/ostad/tamarin'>tamarin<a/>"
    b="<a href='/ostad/videoha'>videoha<a/>"
    return HttpResponse(a+ '\t\t\t\t'+b)

def tamarin(request):
    return render(request,'tamarin.html')

def videoha(request):
    return HttpResponse('videoha')
