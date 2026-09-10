from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.views.generic.detail import SingleObjectMixin


class BookingAccessRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SingleObjectMixin
):
    """
    Перевіряє, чи має користувач доступ до перегляду
    або скасування бронювання.
    1. Клієнт, який створив бронювання.
    2. Власник готелю, у якому заброньовано кімнату.
    3. Суперкористувач.
    """

    def test_func(self):
        booking = self.get_object()
        user = self.request.user

        is_client = booking.user == user
        is_hotel_owner = booking.room.hotel.owner == user

        return is_client or is_hotel_owner or user.is_superuser