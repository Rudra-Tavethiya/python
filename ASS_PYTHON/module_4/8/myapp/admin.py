from django.contrib import admin
from myapp.models import *

# Register your models here.
class doctordetails(admin.ModelAdmin):
    list_display = ("name","email","phone")

admin.site.register(doctor,doctordetails)