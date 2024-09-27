from django.urls import path
from .views import (
    DeveloperListView,
    DeveloperDetailView,
    PropertyListView,
    PropertyDetailView,
)

urlpatterns = [
    path('zastroyshiki/', DeveloperListView.as_view(), name='developer-list'),
    path('zastroyshiki/<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),
    path('novostroyki/', PropertyListView.as_view(), name='property-list'),  # Список всех новостроек
    path('novostroyki/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),  # Детальная стра
]
