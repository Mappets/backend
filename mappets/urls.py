from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers, permissions
from rest_framework.authtoken.views import obtain_auth_token

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from mappets.apps.organizations.views import OrganizationViewSet
from mappets.apps.pets.views import (PetViewSet, PetHistoryViewSet,
        PetBreedViewSet, PetGenderViewSet,
        PetColorViewSet, PetSizeViewSet,
        PetSpecieViewSet)
from mappets.apps.users.views import UserViewSet, RegisterUserView, MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
      title="Mappets API",
      default_version='v1',
      description="Interface de teste para consumo da API Mappets V1",
      terms_of_service="http://api.mappets.app/",
      contact=openapi.Contact(email="contato@mappets.app"),
      license=openapi.License(name="BSD License"),
   ),
#    public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    path('api/v1/pets/', include('mappets.apps.pets.urls')),
    path('api/v1/', include(router.urls)),
    # path('api-token-auth/', obtain_auth_token),
    path('api/v1/register/', RegisterUserView.as_view(), name='register'),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO: Usar i18n_patterns (já importado) para usar multilanguage na API DRF
# https://fueled.com/blog/supporting-multiple-languages-in-django/

urlpatterns += i18n_patterns(
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    prefix_default_language=False,
)
