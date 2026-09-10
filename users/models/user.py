from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """
    Кастомна модель користувача.
    Розширює стандартну модель AbstractUser додатковим
    полем ролі та допоміжними властивостями.
    """

    ROLES_CHOICES = [
        ('guest', _('Клієнт')),
        ('owner', _('Власник готелю')),
        ('admin', _('Адміністратор')),
    ]

    role = models.CharField(
        verbose_name=_('Роль'),
        max_length=20,
        choices=ROLES_CHOICES,
        default='guest',
    )

    @property
    def is_guest(self) -> bool:
        return self.role == 'guest'

    @property
    def is_hotel_owner(self) -> bool:
        return (self.role == 'owner' or
                self.is_superuser)

    @property
    def is_admin_user(self) -> bool:
        return (self.role == 'admin' or
                self.is_superuser)
