from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    LoginAPIView,
    LogoutAPIView,
)

app_name = 'users'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login_user'),
    path('logout/', LogoutAPIView.as_view(), name="logout_user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]