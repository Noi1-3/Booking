from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _l

from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
)

from ..forms import RoomForm
from ..models import Room

from ..mixins.room import (
    RoomCreateMixin,
    RoomOwnerRequiredMixin,
)


class RoomCreateView(
    SuccessMessageMixin,
    RoomCreateMixin,
    CreateView
):
    """Створення кімнати конкретного готелю."""

    model = Room
    form_class = RoomForm
    template_name = 'hotels/room_form.html'

    success_message = _l(
        "Кімнату №%(room_number)s "
        "успішно додано."
    )

    def get_success_url(self):
        return reverse_lazy(
            'hotel_detail',
            kwargs={'pk': self.hotel.pk}
        )


class RoomUpdateView(
    SuccessMessageMixin,
    RoomOwnerRequiredMixin,
    UpdateView
):
    """Редагування конкретної кімнати."""

    model = Room
    form_class = RoomForm
    template_name = 'hotels/room_form.html'

    success_message = _l(
        "Інформацію про кімнату №%(room_number)s "
        "успішно оновлено."
    )

    def get_success_url(self):
        return reverse_lazy(
            'hotel_detail',
            kwargs={'pk': self.object.hotel.pk}
        )


class RoomDeleteView(
    RoomOwnerRequiredMixin,
    DeleteView
):
    """Видалення конкретної кімнати."""

    model = Room
    template_name = 'hotels/room_confirm_delete.html'

    def form_valid(self, form):
        messages.success(
            self.request,
            _("Кімнату №%(room_number)s успішно видалено.") %
            {'room_number': self.object.room_number}
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'hotel_detail',
            kwargs={'pk': self.object.hotel.pk}
        )
