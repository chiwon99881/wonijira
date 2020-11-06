from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages


def user_login(request):
    if request.method == "GET":

        return render(request, "auth/login.html")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome WoniJIRA")
            return redirect(reverse("core:home"))
        else:
            messages.error(request, "Username or Password was wrong.")
            return render(request, "auth/login.html", context={"username": username})


def user_logout(request):
    logout(request)
    return redirect(reverse("core:home"))
