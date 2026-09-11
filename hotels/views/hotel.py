from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F, Min, Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _l

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from ..forms import HotelForm
from ..models import Hotel

from ..mixins.hotel import (
    HotelCreateMixin,
    HotelOwnerRequiredMixin,
)


class HotelListView(ListView):
    """
    Отримання всіх готелів з пошуком, фільтрацією,
    мінімальною ціною та сортуванням.
    """

    model = Hotel
    template_name = 'hotels/hotel_list.html'
    context_object_name = 'hotels'
    paginate_by = 10

    def get_queryset(self):
        queryset = (
            super().get_queryset()
            .select_related('owner')
            .annotate(
                min_price=Min(
                    'rooms__price_per_night',
                    filter=Q(rooms__is_available=True)
                )
            )
        )

        city = self.request.GET.get('city')
        title = self.request.GET.get('title')

        if city:
            queryset = queryset.filter(city__iexact=city)
        if title:
            queryset = queryset.filter(title__icontains=title)

        sort = self.request.GET.get('sort')

        if sort == 'price_asc':
            queryset = queryset.order_by(F('min_price').asc(nulls_last=True))
        elif sort == 'price_desc':
            queryset = queryset.order_by(F('min_price').desc(nulls_last=True))
        elif sort == 'date_asc':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset


class HotelDetailView(DetailView):
    """Перегляд інформації про готель та його кімнати."""

    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    context_object_name = 'hotel'

    def get_queryset(self):
        return super().get_queryset().annotate(
            min_price=Min(
                'rooms__price_per_night',
                filter=Q(rooms__is_available=True)
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.object.rooms.all()
        return context


class HotelCreateView(
    SuccessMessageMixin,
    HotelCreateMixin,
    CreateView
):
    """Створення нового готелю."""

    model = Hotel
    form_class = HotelForm
    template_name = 'hotels/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

    success_message = _l(
        "Готель '%(title)s' "
        "успішно створено!"
    )


class HotelUpdateView(
    SuccessMessageMixin,
    HotelOwnerRequiredMixin,
    UpdateView
):
    """Редагування конкретного готелю."""

    model = Hotel
    form_class = HotelForm
    template_name = 'hotels/hotel_form.html'

    success_message = _l(
        "Інформацію про готель '%(title)s' "
        "успішно оновлено."
    )

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

    def form_valid(self, form):
        messages.success(
            self.request,
            _("Готель '%(title)s' успішно видалено.") %
            {'title': self.object.title}
        )
        return super().form_valid(form)
