from django.db import models

# Create your models here.

class Person(models.Model):
    primer_nombre = models.CharField(max_length=80)
    segundo_nombre = models.CharField(max_length=80,blank=True)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80)
    identidicacion = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=150)
    correo = models.EmailField(blank=True)

    class Meta:
        abstract = True

class Cliente(Person):
    pass

class Asesor(Person):
    codigo = models.IntegerField()
