from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


class HotelOwnerRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """
    Дозволяє доступ тільки користувачам із роллю
    власника готелю або суперюзерам.
    """

    def test_func(self):
        return self.request.user.is_hotel_owner


class GuestRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """Дозволяє доступ тільки звичайним клієнтам."""

    def test_func(self):
        return self.request.user.is_guest


class AdminRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """Дозволяє доступ тільки адміністраторам."""

    def test_func(self):
        return self.request.user.is_admin_user
