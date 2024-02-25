from rest_framework.routers import SimpleRouter

from Game.views.admin import GameViewSet, CategoryViewSet

router = SimpleRouter()
router.register('game', GameViewSet, basename='Game')
router.register('category', CategoryViewSet, basename='Category')
urlpatterns = [] + router.urls
