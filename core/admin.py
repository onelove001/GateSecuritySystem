from django.contrib import admin
from core.models import *


admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Person)
admin.site.register(Gate)

