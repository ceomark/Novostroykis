from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('properties/', include('properties.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Главная страница
    path('accounts/', include('allauth.urls')),
    path('api/', include('properties.api_urls')),  # Подключение api маршрутов для properties
    path('', include('reviews.urls')),  # для приложения reviews
]
