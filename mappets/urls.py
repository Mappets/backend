from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from mappets.apps.organizations.views import OrganizationViewSet
from mappets.apps.pets.views import (PetViewSet, PetHistoryViewSet,
        PetBreedViewSet, PetGenderViewSet,
        PetColorViewSet, PetSizeViewSet,
        PetSpecieViewSet)
from mappets.apps.users.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_jwt.views import obtain_jwt_token

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
    path('', include('django_populate.urls')),
    # path('api-token-auth/', obtain_auth_token),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('admin/', admin.site.urls),
]

# TODO: Usar i18n_patterns (já importado) para usar multilanguage na API DRF
# https://fueled.com/blog/supporting-multiple-languages-in-django/

urlpatterns += i18n_patterns(
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    prefix_default_language=False,
)
