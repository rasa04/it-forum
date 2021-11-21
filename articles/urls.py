from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("about_us", about_us),
    path("horoscope", horoscope),
]
