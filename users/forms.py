from django import forms

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)

from utils.mixins import BootstrapFormMixin
from .models import User


class CustomUserCreationForm(
    BootstrapFormMixin,
    UserCreationForm
):
    """Форма реєстрації нового користувача."""

    placeholders = {
        'username': "Ім'я користувача",
        'email': "Електронна пошта",
        'password1': "Введіть пароль",
        'password2': "Повторіть пароль",
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'role'
        )


class UserProfileForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма оновлення даних користувача."""

    placeholders = {
        'first_name': "Ім'я",
        'last_name': "Прізвище",
        'email': "Електронна пошта",
    }

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )


class CustomPasswordChangeForm(
    BootstrapFormMixin,
    PasswordChangeForm
):
    """Форма зміни пароля користувача."""

    placeholders = {
        'old_password': "Введіть старий пароль",
        'new_password1': "Введіть новий пароль",
        'new_password2': "Повторіть новий пароль",
    }


class CustomLoginForm(
    BootstrapFormMixin,
    AuthenticationForm
):
    """Форма авторизації користувача."""

    placeholders = {
        'username': "Логін",
        'password': "Пароль",
    }
