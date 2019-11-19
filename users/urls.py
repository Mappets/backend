from django.urls import path
from users.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# Users API routes
router.register('users/', UserViewSet)

urlpatterns = router.urls