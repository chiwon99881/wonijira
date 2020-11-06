from django.shortcuts import render
from django.contrib import messages


def login(request):
    if request.method == "GET":
        messages.success(request, "TEST SUCCESS MESSAGE.")
        return render(request, "auth/login.html")
