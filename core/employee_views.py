from django.urls import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import time


def employee_dashboard(request):
    return render(request, "core/index.html", {})


@login_required
def create_public(request):
    choices = ["Student", "Staff", "New visitor"]
    gates = Gate.objects.all()
    context = {"choices":choices, "gates":gates}
    return render(request, "core/create_person.html", context)


def create_public_save(request):
    if request.method=="POST":
        name = request.POST["name"]
        type = request.POST["type"]
        gate = request.POST["gate"]
        car_model_name = request.POST["car_model_name"]
        car_number = request.POST["car_number"]
        person_id = str(hash(time.time()))[:12]
        try:
            gate_id = Gate.objects.get(id = gate)
            person = Person(person_id = int(person_id), full_name=name, type=type, car_number=int(car_number), car_model_name=car_model_name, registered_by=request.user.employee, gate_id=gate_id)
            person.save()
            messages.success(request, f"Creation Success!")
            return redirect("create_public")
        except:
            messages.error(request, "Creation Failed")
            return redirect("create_public")


@csrf_exempt
def check_car_number(request):
    car_number = request.POST.get("car_number")
    print(car_number)
    check_if = Person.objects.filter(car_number = car_number).exists()
    if check_if:
        return HttpResponse("True")
    else:
        return HttpResponse("False")


@login_required
def manage_persons(request):
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
    return render(request, "core/manage_persons.html", context)


@login_required
def edit_person(request, person_id):
    person = Person.objects.filter(person_id = person_id).first()
    gates = Gate.objects.all()
    employees = Employee.objects.all()
    choices = ["Student", "Staff", "New visitor"]
    context = {"person":person, "choices":choices, "gates":gates, "employees":employees}
    return render(request, "core/edit_person.html", context)


def edit_person_save(request):
    if request.method=="POST":
        name = request.POST["name"]
        type = request.POST["type"]
        gate = request.POST["gate"]
        car_model_name = request.POST["car_model_name"]
        car_number = request.POST["car_number"]
        person_id = request.POST["person_id"]
        try:
            person = Person.objects.get(person_id = person_id)
            gate_id = Gate.objects.get(id = gate)
            person.full_name = name
            person.type = type
            person.gate_id = gate_id
            person.car_model_name = car_model_name
            person.car_number = car_number
            person.save()
            messages.success(request, f"Creation Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Creation Failed")
            return redirect(request.META.get("HTTP_REFERER"))






            

