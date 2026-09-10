from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)

from ..forms import RoomForm
from ..models import Room

from ..mixins.room import (
    RoomCreateMixin,
    RoomOwnerRequiredMixin,
)


class RoomCreateView(
    RoomCreateMixin,
    CreateView
):
    """Створення кімнати конкретного готелю."""

    model = Room
    form_class = RoomForm
    template_name = 'hotels/room_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'hotel_detail',
            kwargs={'pk': self.hotel.pk}
        )


class RoomUpdateView(
    RoomOwnerRequiredMixin,
    UpdateView
):
    """Редагування конкретної кімнати."""

    model = Room
    form_class = RoomForm
    template_name = 'hotels/room_form.html'

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

    def get_success_url(self):
        return reverse_lazy(
            'hotel_detail',
            kwargs={'pk': self.object.hotel.pk}
        )
