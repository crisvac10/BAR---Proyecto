from django.db import models

# Create your models here.

class Cliente(models.Model):
  
    DOC_CHOICES=(
       ('0', 'CC'),
       ('1', 'CE'),
       ('2', 'Pasaporte')
    )

    name = models.CharField('Nombre',max_length=60 )
    last_name1 = models.CharField('Primer Apellido',max_length=60)
    tipo_documento = models.CharField ('Tipo documento', max_length=1, choices=DOC_CHOICES)
    num_doc = models.IntegerField('Numero de documento')
    telefono = models.IntegerField('Telefono', null=True)
    
    def __str__(self):
     return str(self.id) + ' - '+ self.name + ' - ' + self.last_name1