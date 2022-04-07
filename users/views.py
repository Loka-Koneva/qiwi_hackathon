# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.shortcuts import render
#
#
# class LoginUser(LoginView):
#     # form_class = AuthenticationForm
#     # template_name = "qiwi_hackathon_frontend/login.html"
#     template_name = '/home/loka/Documents/GitHub/hackathon/qiwi_hackathon/rest_framework/registration/login.html'

from .models import User
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    LoginSerializer,
    LogoutSerializer,
)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    template_name = '/home/loka/Documents/GitHub/hackathon/qiwi_hackathon/rest_framework/registration/login.html'

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
