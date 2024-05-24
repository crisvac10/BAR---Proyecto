from django.contrib import admin
from .models import Inventario

# Register your models here.


#class InventarioAdmin(admin.ModelAdmin):
    
  
    
class InventarioAdminOne(admin.ModelAdmin):
    list_display=(
        'categoria',
        'name_bebida',
        'tamaño',
        'cantidad',
    )
    search_fields=(
        'name_bebida',
    )
    list_filter=(
       'categoria',
       'name_bebida',
       'tamaño',
     'cantidad',
    )
admin.site.register(Inventario,InventarioAdminOne)

