from rest_framework.authtoken.views import ObtainAuthToken

from user.serializer import AdminLoginSerializer


class AdminLoginView(ObtainAuthToken):
    serializer_class = AdminLoginSerializer
