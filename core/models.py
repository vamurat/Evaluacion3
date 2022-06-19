from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models



class Categoria(models.Model):
    idCategoria = models.IntegerField(default=0)
    nombreCategoria = models.CharField(max_length=200)


class Producto(models.Model):
    idProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    Descripcion = models.CharField(max_length=200)
    