from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from organizations.views import OrganizationViewSet
from pets.views import PetViewSet, PetHistoryViewSet, PetBreedViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()

# Organizations API routes
router.register('organizations', OrganizationViewSet)
router.register('users', UserViewSet, basename="users")
router.register('pets', PetViewSet, basename='pets')
router.register('breeds', PetBreedViewSet, basename='breeds')
router.register('history', PetHistoryViewSet, basename='history')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
