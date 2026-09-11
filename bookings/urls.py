from django.urls import path

from .views import (
    BookingCreateView,
    UserBookingListView,
    HotelOwnerBookingListView,
    BookingCancelView,
)


urlpatterns = [
    path('room/<int:room_pk>/create/', BookingCreateView.as_view(),         name='booking_create'),
    path('my/',                        UserBookingListView.as_view(),       name='user_booking_list'),
    path('owner/',                     HotelOwnerBookingListView.as_view(), name='owner_booking_list'),
    path('<int:pk>/delete/',           BookingCancelView.as_view(),         name='booking_delete'),
]
