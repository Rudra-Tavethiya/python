from django.contrib import admin
from app.models import *
# Register your models here.

class allname(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(department,allname)
admin.site.register(stid)
admin.site.register(student,allname)
admin.site.register(subject,allname)
admin.site.register(marks)