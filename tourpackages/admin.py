from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Register)
admin.site.register(RentCar)
# admin.site.register(CustomUser)

#
# from django.contrib import admin
# from django.contrib.admin.models import LogEntry
#
# admin.site.unregister(LogEntry)
# tourpackages/admin.py

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomLogEntry(LogEntry):
    class Meta:
        proxy = True

admin.site.register(CustomLogEntry)
