from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _l


class AnonymousRequiredMixin(AccessMixin):
    """Забороняє доступ авторизованим користувачам."""

    redirect_url = 'profile'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(
                request,
                _l("Ви вже авторизовані в системі.")
            )
            return redirect(self.redirect_url)

        return super().dispatch(request, *args, **kwargs)
