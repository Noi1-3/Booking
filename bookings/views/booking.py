from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
)

from hotels.models import Room
from bookings.forms.booking import BookingForm
from bookings.models.booking import Booking
from bookings.services.booking import create_booking
from ..mixins import BookingAccessRequiredMixin


class BookingCreateView(
    LoginRequiredMixin,
    CreateView
):
    """Створення нових бронювань для конкретної кімнати."""

    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.room = get_object_or_404(Room, pk=self.kwargs['room_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        check_in = form.cleaned_data['check_in_date']
        check_out = form.cleaned_data['check_out_date']

        try:
            self.object = create_booking(
                user=self.request.user,
                room=self.room,
                check_in=check_in,
                check_out=check_out,
            )
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = self.room
        return context

    def get_success_url(self):
        return reverse_lazy(
            'booking_detail',
            kwargs={'pk': self.object.pk}
        )


class BookingDetailView(
    BookingAccessRequiredMixin,
    DetailView
):
    """Детальний перегляд конкретного бронювання."""

    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'


class UserBookingListView(
    LoginRequiredMixin,
    ListView
):
    """Список всіх бронювань поточного користувача."""

    model = Booking
    template_name = 'bookings/user_booking_list.html'
    context_object_name = 'bookings'
    paginate_by = 10

    def get_queryset(self):
        return (
            Booking.objects.filter(user=self.request.user)
            .select_related('room', 'room__hotel')
            .order_by('-created_at')
        )


class HotelOwnerBookingListView(
    LoginRequiredMixin,
    ListView
):
    """Список бронювань у готелях, що належать власнику."""

    model = Booking
    template_name = 'bookings/owner_booking_list.html'
    context_object_name = 'bookings'
    paginate_by = 10

    def get_queryset(self):
        return (
            Booking.objects.filter(room__hotel__owner=self.request.user)
            .select_related('user', 'room', 'room__hotel')
            .order_by('-created_at')
        )


class BookingCancelView(
    BookingAccessRequiredMixin,
    DeleteView
):
    """Скасування/видалення бронювання."""

    model = Booking
    template_name = 'bookings/booking_confirm_cancel.html'
    success_url = reverse_lazy('user_booking_list')