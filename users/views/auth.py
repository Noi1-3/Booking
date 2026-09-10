from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
)

from users.forms.auth import (
    CustomUserCreationForm,
    CustomLoginForm,
    CustomPasswordChangeForm,
)

from ..mixins import AnonymousRequiredMixin


class RegisterView(
    AnonymousRequiredMixin,
    CreateView
):
    """Реєстрація нового користувача."""

    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(
    AnonymousRequiredMixin,
    LoginView
):
    """Авторизація користувача."""
    form_class = CustomLoginForm
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    """Вихід із системи."""
    next_page = reverse_lazy('login')


class UserPasswordChangeView(PasswordChangeView):
    """Зміна пароля поточного користувача."""
    form_class = CustomPasswordChangeForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('profile')
