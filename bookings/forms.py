from datetime import date
from django import forms
from django.utils import timezone

from utils.mixins import BootstrapFormMixin
from .models import Booking


class BookingForm(
    BootstrapFormMixin,
    forms.ModelForm
):
    """Форма для створення бронювання кімнати."""

    class Meta:
        model = Booking
        fields = (
            'check_in_date',
            'check_out_date'
        )
        widgets = {
            'check_in_date':  forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        """Валідація дат заїзду та виїзду."""
        cleaned_data = super().clean()

        if cleaned_data is None:
            return cleaned_data

        check_in = cleaned_data.get('check_in_date')
        check_out = cleaned_data.get('check_out_date')

        if (
            isinstance(check_in, date) and
            isinstance(check_out, date)
        ):
            today = timezone.now().date()

            if check_in < today:
                self.add_error(
                    'check_in_date',
                    "Дата заїзду не може бути в минулому."
                )

            if check_out <= check_in:
                self.add_error(
                    'check_out_date',
                    "Дата виїзду повинна бути пізнішою за дату заїзду."
                )

        return cleaned_data
