from django.shortcuts import *
from django.urls import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin, logout as dlogout
from django.contrib import messages

from core.models import CustomUser



def login_page(request):
    context = {}
    return render(request, "login.htm", context)


def login_user(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            dlogin(request, user)
            if user.user_type == '1':
                return redirect("admin_dashboard")

            elif user.user_type == '2':
                return redirect('employee_dashboard')

        else:
            messages.error(request, "Invalid Login Details! ")
            return redirect("login_page")

    messages.error(request, "Method Not Allowed")
    return redirect("login_page")


def logout_page(request):
    dlogout(request)
    return redirect("employee_dashboard")

