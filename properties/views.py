from rest_framework import generics, permissions
from .models import Developer, Property
from .serializers import DeveloperSerializer, PropertySerializer

# Список всех застройщиков
class DeveloperListView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [permissions.AllowAny]

# Детальная информация о застройщике
class DeveloperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [permissions.AllowAny]

# Список объектов недвижимости
class PropertyListView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]

# Детальная информация о конкретном объекте недвижимости
class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]
