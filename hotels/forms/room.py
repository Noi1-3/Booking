from django import forms

from utils.mixins import BootstrapFormMixin
from ..models import Room


class RoomForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма створення та редагування кімнати."""

    placeholders = {
        'room_number': 'Наприклад: 101 або Люкс-2',
        'price_per_night': 'Наприклад: 1500.00',
    }

    class Meta:
        model = Room
        fields = (
            'room_number',
            'price_per_night',
            'is_available'
        )