from django.urls import path
from organizations.views import OrganizationViewSet, OrganizationHistoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# organizations API routes
router.register('organizations', OrganizationViewSet, basename='organizations')
router.register('organizations/history', OrganizationHistoryViewSet, basename='history')

urlpatterns = router.urls