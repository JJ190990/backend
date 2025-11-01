from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Producto
        fields = ['id','nombre','descripcion','precio','stock','categoria','marca','genero','imagen',]