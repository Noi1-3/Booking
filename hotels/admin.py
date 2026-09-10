from django.contrib import admin
from .models import Hotel, Room


class RoomInline(admin.TabularInline):
    """Управління кімнатами у формі готелю."""
    model = Room
    extra = 1

    fields = (
        'room_number',
        'price_per_night',
        'is_available'
    )


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    """Адмінка для управління готелями."""

    list_display = (
        'title',
        'owner',
        'city',
        'address',
        'created_at'
    )

    list_filter = (
        'city',
        'created_at'
    )

    search_fields = (
        'title',
        'city',
        'address',
        'owner__username'
    )

    inlines = [RoomInline]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Адмінка для управління номерами."""

    list_display = (
        'room_number',
        'hotel',
        'price_per_night',
        'is_available'
    )

    list_filter = (
        'is_available',
        'hotel__city'
    )

    search_fields = (
        'room_number',
        'hotel__title'
    )
