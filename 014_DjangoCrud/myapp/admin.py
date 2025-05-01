from django.contrib import admin
from myapp.models import *

# Register your models here.

class studentdisply(admin.ModelAdmin):
    list_display = ("username","email","phone","age")

admin.site.register(student,studentdisply)