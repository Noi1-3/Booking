from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

from .hotel import Hotel


class Room(models.Model):
    """
    Модель кімнати в готелі.
    Зберігає номер кімнати, поточну вартість
    за добу та прапорець доступності.
    """
    
    hotel = models.ForeignKey(
        to=Hotel, 
        on_delete=models.CASCADE, 
        related_name='rooms',
        verbose_name=_('Готель'),
    )

    room_number = models.CharField(
        verbose_name=_('Номер кімнати'),
        max_length=50,
    )

    price_per_night = models.DecimalField(
        verbose_name=_('Ціна за ніч'),
        max_digits=10, 
        decimal_places=2,
        validators=[
            MinValueValidator(
                Decimal('0.01'),
                message=_('Ціна за ніч має бути щонайменше '
                          '%(limit_value)s.')
            ),
            MaxValueValidator(
                Decimal('1000000.00'), 
                message=_('Ціна за ніч не може перевищувати '
                          '%(limit_value)s.')
            ),
        ],
    )
    
    is_available = models.BooleanField(
        verbose_name=_('Доступність'),
        default=True,
    )

    class Meta:
        verbose_name = _('Кімната')
        verbose_name_plural = _('Кімнати')
        constraints = [
            models.UniqueConstraint(
                fields=['hotel', 'room_number'],
                name='unique_room_per_hotel'
            )
        ]

    def __str__(self):
        return f"{self.hotel.title} - {self.room_number}"
