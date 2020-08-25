from django.urls import path, include
from rest_framework import routers

from mappets.apps.pets.views import PhotoUploadView


urlpatterns = [
    path('photos/', PhotoUploadView.as_view()),
]
