from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm,LoginForm2
from django.http import HttpResponse

def home(request):
    a="""<a href='/ologin'>ostad<a/>
    
    <a href='/dlogin'>daneshjoo<a/>
    """
    return HttpResponse(a)

def ologin(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        login(request, user)
        context["form"] = LoginForm()
        return redirect('/ostad')

    return render(request, "ologin.html", context)

def dlogin(request):
    form = LoginForm2(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        studentNum = form.cleaned_data.get("studentNum")
        user = authenticate(request, email=email, password=password,studentNum=studentNum)
        login(request, user)
        context["form"] = LoginForm()
        return redirect('/daneshjoo')

    return render(request, "ologin.html", context)