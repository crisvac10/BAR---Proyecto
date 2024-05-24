from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display=(
        'categoria',
        'name_bebida',
        'precio',
        
    )
    search_fields=(
        'name_bebida',
    )
    list_filter=(
       'categoria',
       'name_bebida',
       'precio',
    )
admin.site.register(Menu, MenuAdmin)


