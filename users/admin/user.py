from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models.user import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Адмінка для користувачів та їхніх ролей."""

    list_display = (
        'username',
        'email',
        'role',
        'is_staff',
        'is_active'
    )

    list_filter = (
        'role',
        'is_staff',
        'is_active'
    )

    search_fields = (
        'username',
        'email'
    )

    ordering = (
        'username',
    )
