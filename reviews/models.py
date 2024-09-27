from django.db import models
from authentication.models import User
from properties.models import Developer, Property

# Модель отзывов для модуль reviews
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')  # Уникальное related_name
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='object_reviews', blank=True, null=True)  # Уникальное related_name
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='builder_reviews', blank=True, null=True)  # Уникальное related_name
    rating = models.IntegerField()  # Рейтинг (звёзды)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.email} for {'Developer' if self.developer else 'Property'}"
