from django import forms

from utils.mixins import BootstrapFormMixin
from .models import Hotel, Room


class HotelForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма створення та редагування готелю."""

    placeholders = {
        'title': 'Наприклад: Grand Hotel',
        'city': 'Наприклад: Київ',
        'address': 'Вулиця, номер будинку',
        'description': 'Опишіть особливості та переваги готелю...',
    }

    class Meta:
        model = Hotel
        fields = (
            'title',
            'city',
            'address',
            'description'
        )
        widgets = {
            'address':     forms.Textarea(attrs={'rows': 2}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


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
