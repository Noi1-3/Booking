from .hotel import (
    HotelListView,
    HotelDetailView,
    HotelCreateView,
    HotelUpdateView,
    HotelDeleteView,
)

from .room import (
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
)

__all__ = [
    'HotelListView',
    'HotelDetailView',
    'HotelCreateView',
    'HotelUpdateView',
    'HotelDeleteView',
    'RoomCreateView',
    'RoomUpdateView',
    'RoomDeleteView',
]