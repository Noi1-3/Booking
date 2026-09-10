from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


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
        verbose_name=_("Власник"),
    )

    title = models.CharField(
        verbose_name=_("Назва"),
        max_length=255,
    )

    description = models.TextField(
        verbose_name=_("Опис"),
        blank=True, 
        null=True,
    )

    address = models.TextField(
        verbose_name=_("Адреса"),
    )

    city = models.CharField(
        verbose_name=_("Місто"),
        max_length=100,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Дата створення"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Готель")
        verbose_name_plural = _("Готелі")

    def __str__(self):
        return self.title
