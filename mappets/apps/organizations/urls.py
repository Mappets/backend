from django.urls import path
from organizations.views import OrganizationViewSet, OrganizationHistoryViewSet
from rest_framework import routers
from mappets.urls import router

# organizations API routes
router.register('organizations', OrganizationViewSet, basename='organizationsteste')
router.register('organizations/history', OrganizationHistoryViewSet, basename='history')

urlpatterns = router.urls