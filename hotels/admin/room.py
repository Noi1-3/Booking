from django.contrib import admin

from ..models import Room


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
