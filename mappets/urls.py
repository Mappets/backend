from django.contrib import admin
from django.urls import path, include
from pets.views import PetViewSet, PetHistoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pets', PetViewSet, basename='pets')
router.register(
    'pets-history', PetHistoryViewSet, basename='pets-history')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
