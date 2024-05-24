from django.db import models

# Create your models here.

class Factura (models.Model):
 
 Fecha = models.DateTimeField(auto_now_add=True)
