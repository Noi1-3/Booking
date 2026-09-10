from .auth import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    UserPasswordChangeView,
)

from .profile import (
    UserProfileDetailView,
    UserProfileUpdateView,
)

__all__ = [
    'RegisterView',
    'UserLoginView',
    'UserLogoutView',
    'UserPasswordChangeView',
    'UserProfileDetailView',
    'UserProfileUpdateView',
]