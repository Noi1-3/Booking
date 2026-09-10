from django.contrib import admin
from bookings.models.booking import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Адмінка для управління бронюваннями."""

    list_display = (
        'id',
        'user',
        'room',
        'check_in_date',
        'check_out_date',
        'total_price',
        'created_at'
    )

    list_filter = (
        'check_in_date',
        'check_out_date',
        'created_at'
    )

    search_fields = (
        'id',
        'user__username',
        'room__room_number',
        'room__hotel__title'
    )

    readonly_fields = (
        'price_per_night',
        'total_price',
        'created_at'
    )
