from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class ItemMenu(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='establecimientos/platillo', null=False)
    precio = models.CharField(max_length=10, default=0)

Categoria=(
    ('Buffet', 'Buffet'),
    ('Comida rápida', 'Comida rápida'),
    ('Casual', 'Casual'),
    ('De autor', 'De autor'),
    ('Gourmet', 'Gourmet'),
    ('Temático', 'Temático')
)
class Establecimientos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    precio_min = models.CharField(max_length=10)
    precio_max = models.CharField(max_length=50)
    platillo = models.ManyToManyField(ItemMenu)
    parqueadero = models.BooleanField()
    correo = models.EmailField()
    tarjeta_credito = models.BooleanField()
    tarjetas_debito = models.BooleanField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=Categoria, default="Gourmet")
    direccion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='establecimientos/foto-principal', null=False)
    imagen_banner = models.ImageField(upload_to='establecimientos/banner', null=False)
    slug = models.SlugField(unique=True)



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

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.IntegerField()
    comensales = models.IntegerField()
    establecimiento = models.ForeignKey(Establecimientos, on_delete=models.PROTECT)
    creado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True)
    fecha_reserva = models.DateField()
