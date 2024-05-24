from django.db import models

# Create your models here.

class Sede(models.Model):

 name = models.CharField('Nombre', max_length=60, null=True)
 direccion = models.CharField('Dirección', max_length=150, null= True)
 phone = models.IntegerField('Telefono', null=True)

 def __str__(self):
     return str(self.id) + ' - '+ self.name