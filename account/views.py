from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken

from account.serializers import LoginSerializer


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer





