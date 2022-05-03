from django.db import models
import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.


class Categorias(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.nombre

class Servicios(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    fin_semana = models.BooleanField()

    def __str__(self):
        return self.nombre


TIPO_ESTABLECIMIENTO = (
   ('Restaurante', 'Restaurante'),
   ('Cafeteria', 'Cafeteria'),
   ('Bar', 'Bar'),
   ('CafeBar', 'CafeBar')
)
class Establecimientos(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    servicios = models.ForeignKey(Servicios, on_delete=models.PROTECT)
    ciudad = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    rango_precios = models.CharField(max_length=50)
    parqueadero = models.BooleanField()
    correo = models.EmailField()
    tarjeta_credito = models.BooleanField()
    tarjetas_debito = models.BooleanField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_ESTABLECIMIENTO, default='Restaurante')
    direccion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos', null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


class Users(models.Model):
    nombreUsuario = models.CharField(max_length=250, primary_key=True)
    nombres = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    password1 = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreUsuario
