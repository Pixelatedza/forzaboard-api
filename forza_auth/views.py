from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import viewsets
from forza_auth.serializers import UserSerializer
from forza_auth.permissions import IsOwnUserOrReadOnly


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        print(self.action)
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [
                IsAuthenticatedOrReadOnly,
                IsOwnUserOrReadOnly,
            ]

        return [permission() for permission in permission_classes]

