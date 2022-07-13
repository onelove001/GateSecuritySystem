from email import message
from django.shortcuts import *
from django.urls import *
from django.views.decorators.csrf import *
from .models import *
from django.contrib import messages
import uuid
from core.models import Person




def admin_dashboard(request):
    context = {}
    return render(request, "admin_templates/admin_home.htm", context)


def create_employee(request):
    context = {}
    return render(request, "admin_templates/create_employee.htm", context)


def create_admin(request):
    context = {}
    return render(request, "admin_templates/create_admin.html", context)


def create_gate(request):
    context = {}
    return render(request, "admin_templates/create_gate.htm", context)


def create_admin_save(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        try:
            user  = CustomUser.objects.create_user(email = email, username = username, first_name = firstname, last_name = lastname, password = password, user_type = 1)
            user.save()

            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))

        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))



def create_employee_save(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        cell_no = request.POST.get("phone")
        password = request.POST.get("password")
        try:
            user  = CustomUser.objects.create_user(email = email, username = username, first_name = firstname, last_name = lastname, password = password, user_type = 2)
            user.employee.address = address
            user.employee.phone_no = cell_no
            user.employee.gender = gender
            user.save()

            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))

        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))
        

def create_gate_save(request):
    if request.method == "POST":
        gate_name = request.POST.get("gatename")
        gate_unique_id = gate_name.replace(" ", "") + "" + str(uuid.uuid4())
        print(gate_unique_id)
        try:
            gate  = Gate(gate_name = gate_name, gate_unique_id = gate_unique_id)
            gate.save()
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


def manage_employees(request):
    employees = Employee.objects.all()
    context = {"employees":employees}
    return render(request, "admin_templates/manage_employees.htm", context)


def manage_gates(request):
    gates = Gate.objects.all()
    context = {"gates":gates}
    return render(request, "admin_templates/manage_gates.htm", context)


def update_employee(request, employee_id):
    employee = Employee.objects.get(user_id = employee_id)
    context = {"employee":employee}
    return render(request, "admin_templates/update_employee.htm", context)


def update_gate(request, gate_id):
    gate = Gate.objects.get(id = gate_id)
    context = {"gate":gate}
    return render(request, "admin_templates/update_gate.htm", context)


def update_employee_save(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        cell_no = request.POST.get("phone")
        employee = request.POST.get("employee_id")

        try:
            user  = CustomUser.objects.get(id = employee)

            user.email = email
            user.username = username
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            employee = Employee.objects.get(user_id = user.id)
            employee.address = address
            employee.phone_no = cell_no
            employee.gender = gender
            user.save()
            employee.save()
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))

        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


def update_gate_save(request):
    if request.method == "POST":
        gate_name = request.POST.get("gatename")
        gate_no = request.POST.get("gate_no")
        gate_id = request.POST.get("gate_id")
        try:
            gate  = Gate.objects.get(id = gate_id)
            gate.gate_name = gate_name
            gate.gate_no = gate_no
            gate.save()
           
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))

        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


def manage_persons_admin(request):
    search = request.GET.get("table_search")
    if search is not None:
        if Person.objects.filter(car_number = search).exists():
            persons=Person.objects.filter(car_number = search)
        elif Person.objects.filter(person_id = search).exists():
            persons=Person.objects.filter(person_id = search)
        else:
            persons=Person.objects.filter(full_name = search)
        context = {"persons":persons}
    else:
        persons = Person.objects.all()
        context = {"persons":persons}
    return render(request, "admin_templates/manage_persons_admin.html", context)


@csrf_exempt
def check_email(request):
    email = request.POST.get("email")
    check_if = CustomUser.objects.filter(email = email).exists()
    if check_if:
        return HttpResponse("True")
    else:
        return HttpResponse("False")



@csrf_exempt
def check_username(request):
    username = request.POST.get("username")
    check_if = CustomUser.objects.filter(username = username).exists()
    if check_if:
        return HttpResponse("True")
    else:
        return HttpResponse("False")



@csrf_exempt
def check_gatename(request):
    gate_name = request.POST.get("gatename")
    check_if = Gate.objects.filter(gate_name = gate_name).exists()
    if check_if:
        return HttpResponse("True")
    else:
        return HttpResponse("False")