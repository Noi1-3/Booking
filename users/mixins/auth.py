from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin


class AnonymousRequiredMixin(AccessMixin):
    """Забороняє доступ авторизованим користувачам."""

    redirect_url = 'profile'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        return super().dispatch(request, *args, **kwargs)