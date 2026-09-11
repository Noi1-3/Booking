from django.utils.translation import gettext_lazy as _l
from django.contrib import messages

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


class UserIsSelfMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """
    Перевіряє, чи користувач редагує/переглядає
    власний профіль (або є адміністратором).
    """

    def test_func(self):
        user_object = self.get_object()

        return (
            user_object == self.request.user or
            self.request.user.is_superuser
        )

    def handle_no_permission(self):
        messages.error(
            self.request,
            _l("У вас немає прав для редагування "
               "чужого профілю.")
        )
        return super().handle_no_permission()
