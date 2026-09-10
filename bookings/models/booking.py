from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from hotels.models import Room


class Booking(models.Model):
    """
    Модель бронювання кімнати.
    Фіксує дати проживання, статус
    бронювання, а також розраховані
    ціни на момент створення замовлення.
    """

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name=_("Користувач"),
    )

    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name=_("Кімната"),
    )

    check_in_date = models.DateField(
        verbose_name=_("Дата заїзду"),
    )

    check_out_date = models.DateField(
        verbose_name=_("Дата виїзду"),
    )

    price_per_night = models.DecimalField(
        verbose_name=_("Ціна за ніч"),
        max_digits=10,
        decimal_places=2,
        editable=False,
    )

    total_price = models.DecimalField(
        verbose_name=_("Загальна ціна"),
        max_digits=10,
        decimal_places=2,
        editable=False,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Дата створення"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Бронювання")
        verbose_name_plural = _("Бронювання")

    def __str__(self):
        booking_id = self.pk or 'new'
        username = self.user.username if getattr(self, 'user_id', None) else 'unknown'
        return f"Бронювання {booking_id} користувачем {username}"
