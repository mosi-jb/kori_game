from django.urls import path
from rest_framework.routers import SimpleRouter

from user.views import AdminLoginView

router = SimpleRouter()
urlpatterns = [
                  path('login/', AdminLoginView.as_view())
              ] + router.urls
