from django.contrib import admin
<<<<<<< HEAD
from .models import Categorias, Establecimientos, Contacto, Servicios, Menu, Comida
=======
from .models import Categorias, Establecimientos, Contacto, Servicios, Menu, Comida, Reserva
>>>>>>> 4fd5d7e9d25e244a5947246e4a8acce786c89eea
from .forms import EstablecimientosForm

# Register your models here.


class EstablecimientosAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'ciudad', 'categoria', 'parqueadero']
    list_editable = ['parqueadero']
    search_fields = ['nombre']
    list_filter = ['categoria']
    list_per_page = 5
    #form = ProductoForm


admin.site.register(Categorias)
admin.site.register(Establecimientos, EstablecimientosAdmin)
admin.site.register(Contacto)
admin.site.register(Servicios)
admin.site.register(Menu)
admin.site.register(Comida)
<<<<<<< HEAD

=======
admin.site.register(Reserva)
>>>>>>> 4fd5d7e9d25e244a5947246e4a8acce786c89eea
