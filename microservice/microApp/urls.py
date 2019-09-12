from .views import CategoryViewSet, GameViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('game', GameViewSet)

urlpatterns = router.urls

