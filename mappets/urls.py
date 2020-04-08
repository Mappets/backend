from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from organizations.views import OrganizationViewSet
from pets.views import PetViewSet, PetHistoryViewSet

router = routers.DefaultRouter()

# Organizations API routes
router.register('organizations', OrganizationViewSet)
router.register('pets', PetViewSet, basename='pets')
router.register('history', PetHistoryViewSet, basename='history')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
