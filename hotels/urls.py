from django.urls import path

from .views import (
    HotelListView,
    HotelDetailView,
    HotelCreateView,
    HotelUpdateView,
    HotelDeleteView,
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
)


urlpatterns = [
    path('',                 HotelListView.as_view(),   name='hotel_list'),
    path('create/',          HotelCreateView.as_view(), name='hotel_create'),
    path('<int:pk>/',        HotelDetailView.as_view(), name='hotel_detail'),
    path('<int:pk>/update/', HotelUpdateView.as_view(), name='hotel_update'),
    path('<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),

    path('<int:hotel_pk>/rooms/create/', RoomCreateView.as_view(), name='room_create'),
    path('rooms/<int:pk>/update/',       RoomUpdateView.as_view(), name='room_update'),
    path('rooms/<int:pk>/delete/',       RoomDeleteView.as_view(), name='room_delete'),
]