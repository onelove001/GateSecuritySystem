from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender = CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(user_id = instance)
        if instance.user_type == 2:
            Employee.objects.create(user_id = instance)


@receiver(post_save, sender = CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.employee.save()
