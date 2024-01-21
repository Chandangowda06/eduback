import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import CustomUser

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate_password_login(self, attrs):

        data = super().validate(attrs)
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password'),
        }

        if all(credentials.values()):
            user = get_user_model().objects.filter(email=credentials['email']).first()

            if user and user.check_password(credentials['password']):
                data['id'] = user.id
                return data
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)

class CustomUserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 're_password')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        re_password = validated_data.pop('re_password')

        email_pattern = r'^(?:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)?$'
        if not re.match(email_pattern, validated_data.get('email', '')):
            raise serializers.ValidationError({'email': 'Enter a valid email address'})

        if password != re_password:
            raise serializers.ValidationError({'re_password': 'Passwords must match'})

       
        if CustomUser.objects.filter(email=validated_data.get('email', '').lower()).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})

        if len(password) < 6 or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise serializers.ValidationError({'password': 'Password must be at least 6 characters and contain symbols'})
        print("Password")
        validated_data['email'] = validated_data['email'].lower()
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        return user