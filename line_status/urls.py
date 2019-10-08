from django.urls import path

from line_status.views import get, get_delayed_time

urlpatterns = [
    path('status/<line_name>/', get, name='get'),
    path('uptime/<line_name>/', get_delayed_time, name='delayed_time'),
]
