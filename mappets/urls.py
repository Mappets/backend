from django.contrib import admin
from django.urls import path, include
from animal.views import AnimalViewSet, AnimalHistoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('animais', AnimalViewSet, basename='animal')
router.register(
    'animais-history', AnimalHistoryViewSet, basename='animal-history')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
