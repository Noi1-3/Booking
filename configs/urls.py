from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('hotels/', include('hotels.urls')),
    path('bookings/', include('bookings.urls')),


    path('', RedirectView.as_view(url='/hotels/', permanent=True)),
]