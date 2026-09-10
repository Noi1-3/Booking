from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import (
    DetailView,
    UpdateView,
)

from users.forms.auth import UserProfileForm
from users.models.user import User
from ..mixins import UserIsSelfMixin


class UserProfileDetailView(
    LoginRequiredMixin,
    DetailView
):
    """Перегляд профілю користувача."""

    model = User
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile_user'

    def get_object(self, queryset=None):
        if 'pk' not in self.kwargs:
            return self.request.user

        return super().get_object(queryset)


class UserProfileUpdateView(
    UserIsSelfMixin,
    UpdateView
):
    """Редагування даних профілю."""

    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        if 'pk' not in self.kwargs:
            return self.request.user

        return super().get_object(queryset)