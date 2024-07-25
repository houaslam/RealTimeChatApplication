from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='login'),
    path("<str:room_name>/<str:username>/", room_view, name='room'),
]