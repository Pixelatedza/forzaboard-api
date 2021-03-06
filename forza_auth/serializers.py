from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Token claims
class JWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['permissions'] = list(user.get_all_permissions())
        token['isSuperuser'] = user.is_superuser
        token['isStaff'] = user.is_staff
        if user.last_login is not None:
            token['lastLogin'] = user.last_login.isoformat()
        return token


class JWTView(TokenObtainPairView):
    serializer_class = JWTSerializer


# User serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'uuid', 'password', 'email']

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        group = Group.objects.get(name='users')
        user.groups.add(group)
        return user
