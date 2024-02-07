from django.db import models

# Create your models here.


class Locales(models.Model):
    nombre = models.CharField(max_length = 50)
    ubicacion = models.CharField(max_length = 50)

class Productos(models.Model):
    nombre = models.CharField(max_length = 50)
    unidadMedida = models.CharField(max_length = 50)
    tipoProducto = models.CharField(max_length = 50)

class Entregas(models.Model):
    fechaEntrega = models.DateField()
    producto = models.CharField(max_length = 50)
    cantidad = models.IntegerField()

class Repartidor(models.Model):
    nombre = models.CharField(max_length = 50)
    rut = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50)


 