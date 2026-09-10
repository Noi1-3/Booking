from django import forms
from django.utils.translation import gettext_lazy as _

from utils.mixins import BootstrapFormMixin
from ..models import Hotel


class HotelForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма створення та редагування готелю."""

    placeholders = {
        'title':       _('Наприклад: Grand Hotel'),
        'city':        _('Наприклад: Київ'),
        'address':     _('Вулиця, номер будинку'),
        'description': _('Опишіть особливості та переваги готелю...'),
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
