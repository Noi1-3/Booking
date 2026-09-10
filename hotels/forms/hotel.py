from django import forms

from utils.mixins import BootstrapFormMixin
from ..models import Hotel


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
