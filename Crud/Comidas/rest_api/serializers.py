from rest_framework import serializers
from .models import Comida, Local

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comida
        fields='__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Local
        fields='__all__'