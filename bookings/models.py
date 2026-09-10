from django.db import models
from django.contrib.auth.models import User

from ..hotels.models import Room


class Booking(models.Model):
    """
    Модель бронювання кімнати.
    Фіксує дати проживання, статус
    бронювання, а також розраховані
    ціни на момент створення замовлення.
    """

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name="Користувач",
    )

    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name="Кімната",
    )

    check_in_date = models.DateField(
        verbose_name="Дата заїзду",
    )

    check_out_date = models.DateField(
        verbose_name="Дата виїзду",
    )

    price_per_night = models.DecimalField(
        verbose_name="Ціна за ніч",
        max_digits=10,
        decimal_places=2,
        editable=False,
    )

    total_price = models.DecimalField(
        verbose_name="Загальна ціна",
        max_digits=10,
        decimal_places=2,
        editable=False,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата створення",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"

    def __str__(self):
        booking_id = self.id or 'new'
        username = self.user.username if self.user_id else 'unknown'
        return f"Бронювання {booking_id} користувачем {username}"
