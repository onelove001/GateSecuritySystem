
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from GateSecuritySystem import settings
from core.admin_views import *
from core.employee_views import *
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employee_dashboard, name = 'employee_dashboard'),
    path('login', login_page, name = 'login_page'),
    path('login_user', login_user, name = "login_user"),
    path('logout', logout_page, name = 'logout_user'),

    # ADMIN URLS
    path('admin_dashboard', admin_dashboard, name = 'admin_dashboard'),
    path('create_admin', create_admin, name = 'create_admin'),

    path('create_employee', create_employee, name = 'create_employee'),
    path('create_gate', create_gate, name = 'create_gate'),

    path('create_employee_save', create_employee_save, name = 'create_employee_save'),
    path('create_admin_save', create_admin_save, name = 'create_admin_save'),
    path('create_gate_save', create_gate_save, name = 'create_gate_save'),

    path('manage_employees', manage_employees, name = 'manage_employees'),
    path('manage_persons_admin', manage_persons_admin, name = 'manage_persons_admin'),
    path('manage_gates', manage_gates, name = 'manage_gates'),

    path('update_employee/<str:employee_id>', update_employee, name = 'update_employee'),
    path('update_gate/<str:gate_id>', update_gate, name = 'update_gate'),

    path('update_employee_save', update_employee_save, name = 'update_employee_save'),
    path('update_gate_save', update_gate_save, name = 'update_gate_save'),

    path('check_email', check_email, name = "check_email"),
    path('check_username', check_username, name = "check_username"),
    path('check_gatename', check_gatename, name = "check_gatename"),

    # EMPLOYEE URLS
    path('', employee_dashboard, name = "employee_dashboard"),
    path('create', create_public, name = "create_public"),
    path('create_save', create_public_save, name = "create_public_save"),
    path('check_car_number', check_car_number, name = "check_car_number"),
    path('manage_persons', manage_persons, name = "manage_persons"),
    path('edit_person/<person_id>', edit_person, name = "edit_person"),
    path('edit_person_save', edit_person_save, name = "edit_person_save"),

]





urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)