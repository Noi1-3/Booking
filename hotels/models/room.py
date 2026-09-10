from decimal import Decimal
from django.db import models

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
        verbose_name='Готель',
    )

    room_number = models.CharField(
        verbose_name='Номер кімнати',
        max_length=50,
    )

    price_per_night = models.DecimalField(
        verbose_name='Ціна за ніч',
        max_digits=10, 
        decimal_places=2,
        validators=[
            MinValueValidator(
                Decimal('0.01'),
                message='Ціна за ніч має бути щонайменше '
                        '%(limit_value)s.'
            ),
            MaxValueValidator(
                Decimal('1000000.00'), 
                message='Ціна за ніч не може перевищувати '
                        '%(limit_value)s.'
            ),
        ],
    )
    
    is_available = models.BooleanField(
        verbose_name='Доступність',
        default=True,
    )

    class Meta:
        verbose_name = 'Кімната'
        verbose_name_plural = 'Кімнати'
        constraints = [
            models.UniqueConstraint(
                fields=['hotel', 'room_number'],
                name='unique_room_per_hotel'
            )
        ]

    def __str__(self):
        return f"{self.hotel.title} - {self.room_number}"
