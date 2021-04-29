from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import LoginSerializer, RegisterSerializer
from rest_framework import status

from main.permissions import IsAdminPermission
from rest_framework.permissions import IsAuthenticated

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class RegistrationView(APIView):
    permission_classes = [IsAdminPermission, ]
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered', status=status.HTTP_201_CREATED)


class GetRole(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        role = request.user.role
        return Response(f'Role: {role}', status.HTTP_200_OK)






