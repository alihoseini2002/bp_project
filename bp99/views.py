from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ostad="<a href='/ostad'>ostad<a/>"
    return HttpResponse('home page\n\n\n'+ ostad)