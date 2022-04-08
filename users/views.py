from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenRefreshView

from .models import User
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    LoginSerializer,
    LogoutSerializer,
    ServicesSerializer,
    UserSerializer,
)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request: Request) -> Response:
        """Return user after login."""

        user = User.objects.get(username=request.data.get('username'))
        if not user:
            print("Пользователь не найден")
            return Response("Пользователь не найден", status=status.HTTP_400_BAD_REQUEST)
        serializer = LoginSerializer(data=dict(username=request.data.get('username'),
                                               password=request.data.get('password')))
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        """Validate token and save."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        """Return user on GET request."""
        serializer = self.serializer_class(request.user, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ServicesAPIView(APIView):
    serializer_class = ServicesSerializer

    def get(self, request: Request) -> Response:
        # articles = Article.objects.all()
        # serializer = ArticleSerializer(articles, many=True)
        # return Response({"articles": serializer.data})
        pass


class ServicesHistoryAPIView(APIView):
    def get(self, request: Request) -> Response:
        # articles = Article.objects.all()
        # serializer = ArticleSerializer(articles, many=True)
        # return Response({"articles": serializer.data})
        pass

