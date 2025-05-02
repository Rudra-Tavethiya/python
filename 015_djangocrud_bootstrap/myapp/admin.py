from django.contrib import admin
from myapp.models import *
# Register your models here.

class studentdetails(admin.ModelAdmin):
    list_display = ("username","email","phone","age","image")


admin.site.register(student,studentdetails)