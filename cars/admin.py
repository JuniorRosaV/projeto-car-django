from django.contrib import admin
from cars.models import Car, Brand

class Caradmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year','value',)
    search_fields = ('model','brand',)

admin.site.register(Car,Caradmin) 

class Brandadmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Brand,Brandadmin)
