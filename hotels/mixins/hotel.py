from django.http import HttpRequest
from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


class HotelOwnerRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SingleObjectMixin
):
    """Перевіряє, чи є користувач власником готелю."""

    request: HttpRequest

    def test_func(self):
        hotel = self.get_object()
        return hotel.owner == self.request.user


class HotelCreateMixin(LoginRequiredMixin):
    """
    Автоматично призначає поточного авторизованого
    користувача власником створюваного готелю.
    """

    request: HttpRequest

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
