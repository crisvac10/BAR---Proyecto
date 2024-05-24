from django.db import models
from aplication.inventario.models import Inventario
# Create your models here.

class Pedido(models.Model):
     
     id_bebidas = models.ForeignKey(Inventario, on_delete=models.CASCADE)
     cantidad = models.IntegerField('Cantidad')

    

     def __str__(self):
        return str(self.id) + ' - '+ self.id_bebidas + ' - ' + self.cantidad