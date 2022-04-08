from django.contrib.auth import authenticate
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, Service


class RegistrationSerializer(serializers.ModelSerializer[User]):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
        ]


class LoginSerializer(serializers.ModelSerializer[User]):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        """Get user token."""
        user = User.objects.get(email=obj.email)

        return {'refresh': user.tokens['refresh'], 'access': user.tokens['access']}

    class Meta:
        model = User
        fields = ['email', 'username', 'tokens']

    def validate(self, data):  # type: ignore
        """Validate and return user login."""
        username = data['username']
        password = data['password']
        if username is None:
            raise serializers.ValidationError('Введите e-mail для авторизации')

        if password is None:
            raise serializers.ValidationError('Введите логин для авторизации')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Пользователя с таким e-mail и паролем не существует')

        return user


class UserSerializer(serializers.ModelSerializer[User]):
    """Handle serialization and deserialization of User objects."""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'tokens',
        )
        read_only_fields = ('tokens',)


class LogoutSerializer(serializers.Serializer[User]):
    refresh = serializers.CharField()

    def validate(self, attrs):  # type: ignore
        """Validate token."""
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):  # type: ignore
        """Validate save backlisted token."""

        try:
            RefreshToken(self.token).blacklist()

        except TokenError as ex:
            raise exceptions.AuthenticationFailed(ex)


class ServicesSerializer(serializers.Serializer[Service]):
    pass