
from django.contrib import admin
from cars.models import Car, Marca

class MarcaAdmin(admin.ModelAdmin):
   list_display  = ('name',)
   search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):

   list_display = ('modelo', 'marca', 'ano_de_fabricacao', 'ano_de_modelo', 'valor')
   search_fields = ('modelo', 'marca')

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Car, CarAdmin)
