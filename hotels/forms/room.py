from django import forms
from django.utils.translation import gettext_lazy as _

from utils.mixins import BootstrapFormMixin
from ..models import Room


class RoomForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма створення та редагування кімнати."""

    placeholders = {
        'room_number':     _('Наприклад: 101 або Люкс-2'),
        'capacity':        _('Наприклад: 2'),
        'price_per_night': _('Наприклад: 1500.00'),
    }

    class Meta:
        model = Room
        fields = (
            'room_number',
            'capacity',
            'price_per_night',
            'is_available',
        )
