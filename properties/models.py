from django.db import models
from authentication.models import User

# Модель застройщика
class Developer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    founded_year = models.IntegerField()
    website = models.URLField(blank=True, null=True)  # Веб-сайт застройщика
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг застройщика

    def __str__(self):
        return self.name

# Модель объекта недвижимости
class Property(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    region = models.CharField(max_length=100, blank=True, null=True)  # Регион
    city = models.CharField(max_length=100, default='Unknown')  # Город
    address = models.CharField(max_length=255, blank=True, null=True)  # Адрес
    metro_station = models.CharField(max_length=255, blank=True, null=True)  # Ближайшая станция метро
    walking_time_to_metro = models.IntegerField(blank=True, null=True)  # Время пешком до метро (мин)
    transport_time_to_metro = models.IntegerField(blank=True, null=True)  # Время на транспорте до метро (мин)
    number_of_floors = models.IntegerField(blank=True, null=True)  # Этажность здания
    number_of_blocks = models.IntegerField(blank=True, null=True)  # Количество корпусов
    price_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Минимальная цена
    price_per_sqm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Цена за м²
    total_flats = models.IntegerField(blank=True, null=True)  # Общее количество квартир
    construction_class = models.CharField(max_length=50, blank=True, null=True)  # Класс строительства
    completion_date = models.CharField(max_length=50, blank=True, null=True)  # Дата сдачи
    parking = models.CharField(max_length=100, blank=True, null=True)  # Паркинг
    ceiling_height = models.FloatField(blank=True, null=True)  # Высота потолков
    finishing = models.CharField(max_length=100, blank=True, null=True)  # Отделка (без отделки, с отделкой)

    def __str__(self):
        return self.name

# Модель отзывов для объектов недвижимости и застройщиков
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_reviews')  # Пользователь, оставивший отзыв
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_reviews', blank=True, null=True)  # Отзыв об объекте недвижимости
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_reviews', blank=True, null=True)  # Отзыв о застройщике
    rating = models.IntegerField()  # Рейтинг (звёзды)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.email} for {'Developer' if self.developer else 'Property'}"
