from django.db import models
from aplication.sede.models import Sede
# Create your models here.

class Empleado(models.Model):

    Rol_CHOICES=(
       ('0', 'Administrador'),
       ('1', 'Mesero'),
       ('2', 'Cajero'),
       ('3', 'Bartender'),
       ('4', 'Seguridad')
    )

    name = models.CharField('Nombre',max_length=60 )
    last_name1 = models.CharField('Primer Apellido',max_length=60)
    last_name2 = models.CharField('Segundo Apellido',max_length=60)
    rol = models.CharField('Rol',max_length=1, choices=Rol_CHOICES)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
     return str(self.id) + ' - '+ self.name + ' - ' + self.last_name1