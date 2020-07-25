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
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
schema_view = get_swagger_view(title='Mappets API')

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
    path('api/v1/', include(router.urls)),
    # path('api/v1/', include('django_populate.urls')),
    # path('api-token-auth/', obtain_auth_token),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view),
    # path('admin/', admin.site.urls),
]

# TODO: Usar i18n_patterns (já importado) para usar multilanguage na API DRF
# https://fueled.com/blog/supporting-multiple-languages-in-django/

urlpatterns += i18n_patterns(
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    prefix_default_language=False,
)
