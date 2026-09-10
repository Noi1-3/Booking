from django import forms
from django.utils.translation import gettext_lazy as _

from utils.mixins import BootstrapFormMixin
from ..models import User


class UserProfileForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма оновлення даних користувача."""

    placeholders = {
        'first_name': _("Ім'я"),
        'last_name':  _("Прізвище"),
        'email':      _("Електронна пошта"),
    }

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )