from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import *
from django.urls import *


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user = request.user
        
        if user.is_authenticated:

            if user.user_type == "1":
                if modulename == "core.admin_views":
                    pass
                elif modulename == "core.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_dashboard")

            elif user.user_type == "2":
                if modulename == "core.views":
                    pass
                elif modulename == "core.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("employee_dashboard")

        else:
            if request.path == reverse("login_page") or request.path == reverse("login_user") or modulename == "django.contrib.auth.views" or modulename == "core.views":
                pass

            else:
                return redirect("login_page")

