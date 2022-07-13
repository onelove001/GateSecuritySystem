from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_data = (
        (1, "Admin"), 
        (2, "Employee"), 
    )
    user_type = models.CharField(default = 1, choices=user_type_data, max_length = 10)



class Admin(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_id.username


class Employee(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    phone_no = models.CharField(max_length=20)
    sex = (
        ("Male", "Male"), 
        ("Female", "Female"), 
    )
    gender = models.CharField(choices=sex, max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_id.username


class Gate(models.Model):
    gate_name = models.CharField(max_length=20)
    gate_unique_id = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.gate_name


class Person(models.Model):
    person_id = models.CharField(max_length=15, blank=False, unique=True)
    categories = (
        ("Staff", "Staff"), 
        ("Student", "Student"), 
        ("New visitor", "New visitor"), 
    )
    type = models.CharField(choices=categories, max_length=30)
    full_name = models.CharField(max_length=50)
    car_model_name = models.CharField(max_length = 100, blank=False)
    car_number = models.CharField(max_length = 100, unique=True, blank=False)
    registered_by = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="registeremployee")
    gate_id = models.ForeignKey(Gate, on_delete=models.PROTECT, related_name = "person_gate")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ["-created_at"]
        

    def __str__(self):
        return f"{self.full_name}'s {self.car_model_name} Car"

