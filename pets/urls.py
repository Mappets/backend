from django.urls import path
from pets.views import PetViewSet, PetHistoryViewSet
from mappets.urls import router

# Pets API routes
router.register('pets', PetViewSet, basename='pets')
router.register('pets/history', PetHistoryViewSet, basename='history')

urlpatterns = router.urls