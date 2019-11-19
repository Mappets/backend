from django.urls import path
from organizations.views import OrganizationViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# Organizations API routes
router.register('organizations', OrganizationViewSet)

urlpatterns = router.urls