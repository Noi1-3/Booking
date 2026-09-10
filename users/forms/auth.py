from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)

from utils.mixins import BootstrapFormMixin
from users.models.user import User


class CustomUserCreationForm(
    BootstrapFormMixin,
    UserCreationForm
):
    """Форма реєстрації нового користувача."""

    placeholders = {
        'username':  _("Ім'я користувача"),
        'email':     _("Електронна пошта"),
        'password1': _("Введіть пароль"),
        'password2': _("Повторіть пароль"),
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'role'
        )


class CustomPasswordChangeForm(
    BootstrapFormMixin,
    PasswordChangeForm
):
    """Форма зміни пароля користувача."""

    placeholders = {
        'old_password':  _("Введіть старий пароль"),
        'new_password1': _("Введіть новий пароль"),
        'new_password2': _("Повторіть новий пароль"),
    }


class CustomLoginForm(
    BootstrapFormMixin,
    AuthenticationForm
):
    """Форма авторизації користувача."""

    placeholders = {
        'username': _("Логін"),
        'password': _("Пароль"),
    }
