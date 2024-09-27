from rest_framework import serializers
from .models import Developer, Property

# Сериализатор для застройщика
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

# Сериализатор для объекта недвижимости
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
