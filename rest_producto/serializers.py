from rest_framework import serializers
from core.models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =['idProducto','nombre','precio','stock', 'Descripcion']