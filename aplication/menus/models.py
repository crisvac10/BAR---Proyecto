from django.db import models
from aplication.inventario.models import Inventario
# Create your models here.

class Menu (models.Model):
   MEN_CHOICES=(
      ('0', 'WINE AND BEER'),
      ('1', 'COCKTAILS'),
      )
   categoria = models.CharField('Categoria', max_length=1, choices=MEN_CHOICES)
   name_bebida = models.CharField('Nombre bebida', max_length=60, null= False)
   precio = models.PositiveIntegerField('Precio', null= False)
   detalle = models.CharField('Detalle', max_length=100)
   
   def __str__(self):
       return   str(self.id) + ' - '+ self.name_bebida + ' - ' + str(self.precio)