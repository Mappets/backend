from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from organizations.views import OrganizationViewSet
from pets.views import PetViewSet, PetHistoryViewSet, IndexView

router = routers.DefaultRouter()

# Organizations API routes
router.register('organizations', OrganizationViewSet)
router.register('pets', PetViewSet, basename='pets')
router.register('history', PetHistoryViewSet, basename='history')


'''
Define as rotas da aplicação
'''


urlpatterns = [
    path('', IndexView.as_view()),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
