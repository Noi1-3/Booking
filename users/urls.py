from django.urls import path

from .views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    UserPasswordChangeView,
    UserProfileDetailView,
    UserProfileUpdateView,
)


urlpatterns = [
    path('register/',         RegisterView.as_view(),           name='register'),
    path('login/',            UserLoginView.as_view(),          name='login'),
    path('logout/',           UserLogoutView.as_view(),         name='logout'),
    path('password-change/',  UserPasswordChangeView.as_view(), name='password_change'),

    path('profile/',          UserProfileDetailView.as_view(),  name='profile'),
    path('profile/edit/',     UserProfileUpdateView.as_view(),  name='profile_update'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(),  name='profile_detail'),
]
