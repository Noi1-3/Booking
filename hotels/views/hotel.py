from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, F, Min, Q
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

    SORT_OPTIONS = {
        'newest': ('-created_at', 'id'),
        'oldest': ('created_at', 'id'),
        'title_asc': ('title', 'id'),
        'title_desc': ('-title', 'id'),
        'city_asc': ('city', 'title', 'id'),
        'price_asc': (F('min_price').asc(nulls_last=True), 'title', 'id'),
        'price_desc': (F('min_price').desc(nulls_last=True), 'title', 'id'),
        'availability_desc': ('-available_rooms', 'title', 'id'),
    }

    def get_queryset(self):
        queryset = (
            super().get_queryset()
            .select_related('owner')
            .annotate(
                min_price=Min(
                    'rooms__price_per_night',
                    filter=Q(rooms__is_available=True)
                ),
                available_rooms=Count(
                    'rooms',
                    filter=Q(rooms__is_available=True),
                    distinct=True,
                ),
            )
        )

        city = self.request.GET.get('city', '').strip()
        title = self.request.GET.get('title', '').strip()

        if city:
            queryset = queryset.filter(city__iexact=city)
        if title:
            queryset = queryset.filter(title__icontains=title)

        sort = self.request.GET.get('sort', 'newest')
        ordering = self.SORT_OPTIONS.get(sort, self.SORT_OPTIONS['newest'])
        return queryset.order_by(*ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = (
            Hotel.objects.exclude(city='')
            .order_by('city')
            .values_list('city', flat=True)
            .distinct()
        )
        requested_sort = self.request.GET.get('sort', 'newest')
        context['current_sort'] = (
            requested_sort if requested_sort in self.SORT_OPTIONS else 'newest'
        )

        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_string'] = query_params.urlencode()
        return context


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
