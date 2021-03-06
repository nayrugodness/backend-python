from django.contrib import admin
from main.models import Categorias, Establecimientos, Contacto


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



