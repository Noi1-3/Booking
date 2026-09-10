from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from ..forms import HotelForm
from ..models import Hotel

from ..mixins.hotel import (
    HotelCreateMixin,
    HotelOwnerRequiredMixin,
)


class HotelListView(ListView):
    """Отримання всіх готелів з пошуком та фільтрацією."""

    model = Hotel
    template_name = 'hotels/hotel_list.html'
    context_object_name = 'hotels'
    paginate_by = 10

    def get_queryset(self):
        queryset = (
            super().get_queryset()
                   .select_related('owner')
        )

        city = self.request.GET.get('city')
        query = self.request.GET.get('q')

        if city:
            queryset = queryset.filter(city__iexact=city)
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset.order_by('-created_at')


class HotelDetailView(DetailView):
    """Перегляд інформації про готель та його кімнати."""

    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.object.rooms.all()
        return context


class HotelCreateView(
    HotelCreateMixin,
    CreateView
):
    """Створення нового готелю."""

    model = Hotel
    form_class = HotelForm
    template_name = 'hotels/hotel_form.html'
    success_url = reverse_lazy('hotel_list')


class HotelUpdateView(
    HotelOwnerRequiredMixin,
    UpdateView
):
    """Редагування конкретного готелю."""

    model = Hotel
    form_class = HotelForm
    template_name = 'hotels/hotel_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'hotel_detail',
            kwargs={'pk': self.object.pk}
        )


class HotelDeleteView(
    HotelOwnerRequiredMixin,
    DeleteView
):
    """Видалення конкретного готелю."""

    model = Hotel
    template_name = 'hotels/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotel_list')
