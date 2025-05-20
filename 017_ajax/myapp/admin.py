from django.contrib import admin

from.models import *

# Register your models here.
class nameadmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Product, nameadmin)

admin.site.register(country,nameadmin)
admin.site.register(state,nameadmin)
admin.site.register(city,nameadmin)