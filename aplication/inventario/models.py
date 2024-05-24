from django.db import models

# Create your models here.

class Inventario(models.Model):
        CAT_CHOICES=(
               ('0', 'CERVEZA'),
               ('1', 'RON'),
               ('2', 'GIN'),
               ('3', 'VODKA'),
               ('4', 'TEQUILA'),
               ('5', 'BRANDY'),
               ('6', 'AGUARDIENTE'),
               ('7', 'WHISKY'),
               ('8', 'CHAMPAGNA'),
               ('9', 'VINO'),
               ('10', 'COCTEL'),
               )
        
        TAM_CHOICES = (
               ('0', '375 ml'),
               ('1', '750 ml'),
               ('2', '1000 ml'),
               ('3', '210 ml'),
               ('4', '330 ml'),
    )
        categoria = models.CharField('Categoria', max_length=2, choices=CAT_CHOICES)
        name_bebida = models.CharField('Nombre bebida', max_length=60, null= False)
        tamaño = models.CharField('Tamaño', max_length=1, choices=TAM_CHOICES)
        cantidad = models.IntegerField('Cantidad') 

        
        def __str__(self):
         return str(self.id) + ' - '+ self.name_bebida + ' - ' + str(self.cantidad)