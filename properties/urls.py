from django.urls import path
from .views import (
    DeveloperListView,
    DeveloperDetailView,
    PropertyListView,
    PropertyDetailView,
)

urlpatterns = [
    path('developers/', DeveloperListView.as_view(), name='developer-list'),
    path('developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
]
