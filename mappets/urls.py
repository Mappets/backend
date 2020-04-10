from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from organizations.views import OrganizationViewSet
from pets.views import (PetViewSet, PetHistoryViewSet,
PetBreedViewSet, PetGenderViewSet,
PetColorViewSet, PetSizeViewSet,
PetSpecieViewSet)

from users.views import UserViewSet

router = routers.DefaultRouter()

# Organizations API routes
router.register('organizations', OrganizationViewSet)
router.register('users', UserViewSet, basename="users")
router.register('pets', PetViewSet, basename='pets')
router.register('breeds', PetBreedViewSet, basename='breeds')
router.register('genders', PetGenderViewSet, basename='genders')
router.register('colors', PetColorViewSet, basename='colors')
router.register('sizes', PetSizeViewSet, basename='sizes')
router.register('species', PetSpecieViewSet, basename='species')
router.register('history', PetHistoryViewSet, basename='history')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
