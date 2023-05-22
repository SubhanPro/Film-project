from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import Account 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Sorry, this account does not exist.")
    return render(request, "login.html")

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not User.objects.filter(username = username).exists():
            user = User.objects.create_user(username=username, password=password)
            account = Account.objects.create(user = user)
            return redirect("index")
        else:
            messages.info(request, "Sorry, this username is taken.")
    return render(request, "signup.html")

def logout_user(request):
    logout(request)
    return redirect("index")