from django import forms

from utils.mixins import BootstrapFormMixin
from ..models import User


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