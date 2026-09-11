from django.utils.translation import gettext_lazy as _l
from django.contrib import messages

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

    def handle_no_permission(self):
        messages.error(
            self.request,
            _l("Ця сторінка доступна тільки для "
               "власників готелів.")
        )
        return super().handle_no_permission()


class GuestRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """Дозволяє доступ тільки звичайним клієнтам."""

    def test_func(self):
        return self.request.user.is_guest

    def handle_no_permission(self):
        messages.error(
            self.request,
            _l("Ця сторінка доступна тільки для "
               "клієнтів.")
        )
        return super().handle_no_permission()


class AdminRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """Дозволяє доступ тільки адміністраторам."""

    def test_func(self):
        return self.request.user.is_admin_user

    def handle_no_permission(self):
        messages.error(
            self.request,
            _l("Ця сторінка доступна тільки "
               "адміністраторам.")
        )
        return super().handle_no_permission()
