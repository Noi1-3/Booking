from datetime import date
from django.core.exceptions import ValidationError

from users.models.user import User
from bookings.models.booking import Booking, Room


def create_booking(
    user: User,
    room: Room,
    check_in: date,
    check_out: date
) -> Booking:
    """Сервіс, який відповідає за логіку бронювання"""

    if check_in < date.today():
        raise ValidationError(
            "Дата заїзду не може бути в минулому."
        )

    if check_out <= check_in:
        raise ValidationError(
            "Дата виїзду має бути пізнішою за дату заїзду."
        )

    conflicting_bookings = Booking.objects.filter(
        room=room,
        check_in_date__lt=check_out,
        check_out_date__gt=check_in
    )

    if conflicting_bookings.exists():
        raise ValidationError(
            "Ця кімната вже заброньована на вибрані дати."
        )

    nights = (check_out - check_in).days
    price_per_night = room.price_per_night
    total_price = price_per_night * nights

    booking = Booking(
        user=user,
        room=room,
        check_in_date=check_in,
        check_out_date=check_out,
        price_per_night=price_per_night,
        total_price=total_price
    )

    booking.save()
    return booking
