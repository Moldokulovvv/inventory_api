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



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirm = serializers.CharField(min_length=8, write_only=True, required=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confirm')




    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже есть')
        return username


    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm', None)

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user