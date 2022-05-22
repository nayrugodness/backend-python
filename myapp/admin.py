from django.contrib import admin
from .models import Establecimientos, Contacto, Reserva, ItemMenu
from .forms import EstablecimientosForm

# Register your models here.


class EstablecimientosAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'ciudad',  'parqueadero']
    list_editable = ['parqueadero']
    search_fields = ['nombre']

    list_per_page = 5
    #form = ProductoForm


admin.site.register(Establecimientos, EstablecimientosAdmin)
admin.site.register(Contacto)
admin.site.register(Reserva)
admin.site.register(ItemMenu)
