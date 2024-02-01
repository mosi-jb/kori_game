from rest_framework.routers import SimpleRouter

from games.views import GameViewSet, CategoryViewSet

router = SimpleRouter()
router.register('game', GameViewSet, basename='Game')
router.register('category', CategoryViewSet, basename='Category')
urlpatterns = [] + router.urls
