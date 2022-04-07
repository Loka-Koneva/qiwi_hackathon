from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render


class LoginUser(LoginView):
    # form_class = AuthenticationForm
    # template_name = "qiwi_hackathon_frontend/login.html"
    template_name = 'rest_framework/registration/login.html'
