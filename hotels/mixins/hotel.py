from django.contrib import messages
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _l
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
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        messages.error(
            self.request,
            _l("У вас немає прав для редагування "
               "або видалення цього готелю.")
        )
        return super().handle_no_permission()


class HotelCreateMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """
    Автоматично призначає поточного авторизованого
    користувача власником створюваного готелю.
    """

    request: HttpRequest

    def test_func(self):
        return self.request.user.is_hotel_owner

    def handle_no_permission(self):
        messages.error(
            self.request,
            _l("Тільки власники готелів "
               "можуть створювати нові заклади.")
        )
        return super().handle_no_permission()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
