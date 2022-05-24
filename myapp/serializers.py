from django.db.models.query import QuerySet
from .models import Establecimientos, Reserva
from rest_framework import fields, serializers




class EstablecimientosSerializer(serializers.ModelSerializer):

    #nombre_categoria = serializers.CharField(
    #    read_only=True, source='categoria.nombre')


    nombre = serializers.CharField(required=True, min_length=3)

    # def validate_nombre(self, value):
    #     existe = Producto.objects.filter(nombre=value).exists()

    #     if existe:
    #         raise serializers.ValidationError('Este producto ya existe')

    #     else:
    #         return value

    class Meta:
        model = Establecimientos
        fields = '__all__'
        #exclude = ['']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        #exclude = ['']