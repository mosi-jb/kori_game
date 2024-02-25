from rest_framework.routers import SimpleRouter

from Game.views.front import GameFrontViewSet, CategoryFrontViewSet

router = SimpleRouter()
router.register('game', GameFrontViewSet, basename='Game')
router.register('category', CategoryFrontViewSet, basename='Category')
urlpatterns = [] + router.urls
