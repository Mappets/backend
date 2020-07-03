from django.urls import path
from users.views import UserViewSet
from mappets.urls import router

# Users API routes
router.register('users/', UserViewSet)

urlpatterns = router.urls