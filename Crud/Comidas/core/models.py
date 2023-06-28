from django.db import models

# Create your models here.
class Comida(models.Model):
    idComida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    descripcion =models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Local(models.Model):
    idLocal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    comentario =models.CharField(max_length=200)
    ubicacion =models.CharField(max_length=200)

    def __str__(self):
        return self.nombre