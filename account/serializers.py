from django.contrib.auth import authenticate
from rest_framework import serializers

from account.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                message = 'Unable to login with provided credentials'
                raise serializers.ValidationError(message, code='authorization')

        else:
            message = 'Must include "email" and "password"'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs
