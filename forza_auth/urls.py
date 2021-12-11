from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from forza_auth.serializers import JWTView
from forza_auth.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('token', JWTView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
