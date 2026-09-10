from django.db import models
from django.conf import settings


class Hotel(models.Model):
    """
    Модель готелю (об'єкта розміщення).
    Зберігає базові дані про готель, його
    розташування та прив'язку до власника.
    """
    
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='hotels',
        verbose_name='Власник',
    )

    title = models.CharField(
        verbose_name='Назва',
        max_length=255,
    )

    description = models.TextField(
        verbose_name='Опис',
        blank=True, 
        null=True,
    )

    address = models.TextField(
        verbose_name='Адреса',
    )

    city = models.CharField(
        verbose_name='Місто',
        max_length=100,
    )

    created_at = models.DateTimeField(
        verbose_name='Дата створення',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Готель'
        verbose_name_plural = 'Готелі'

    def __str__(self):
        return self.title
