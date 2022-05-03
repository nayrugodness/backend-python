from django.db import models
import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:max_length - 5], randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


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
    tipo = models.CharField(max_length=20, choices=TIPO_ESTABLECIMIENTO, default='Restaurante')
    direccion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos', null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre

@receiver(pre_save, sender=Establecimientos)
def pre_save_receiver(sender, instance, *args, **kwargs):

   if not instance.slug:
       instance.slug = unique_slug_generator(instance)
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
