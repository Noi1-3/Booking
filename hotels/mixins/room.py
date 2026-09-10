from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from ..models import Hotel


class RoomOwnerRequiredMixin(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SingleObjectMixin
):
    """
    Перевіряє, чи є користувач власником готелю,
    якому належить кімната.
    """

    request: HttpRequest

    def test_func(self):
        room = self.get_object()
        return room.hotel.owner == self.request.user


class RoomCreateMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    """
    Отримує об'єкт готелю по ключу.
    Перевіряє права власника готелю.
    Автоматично зв'язує кімнату з готелем
    та додає готель у контекст.
    """

    request: HttpRequest
    hotel: Hotel

    def dispatch(self, request, *args, **kwargs):
        self.hotel = get_object_or_404(Hotel, pk=self.kwargs['hotel_pk'])
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.hotel.owner == self.request.user

    def form_valid(self, form):
        form.instance.hotel = self.hotel
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = self.hotel
        return context