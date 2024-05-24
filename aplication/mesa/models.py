from django.db import models

# Create your models here.

class Mesa(models.Model):
    
    disponible = models.BooleanField('Disponible', default=True)

    def __str__(self):
         return str(self.id) + ' - '+ str(self.disponible) 