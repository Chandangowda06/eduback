from django.shortcuts import render
from users.models import CustomUser
from users.serializers import CustomUserSerializer, UserTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import viewsets

class UserTokenObtainPairView(TokenObtainPairView):
        serializer_class = UserTokenObtainPairSerializer 

        def post(self, request, *args, **kwargs):
            response = super().post(request, *args, **kwargs)

            # Extract user ID from the validated data
            id = self.serializer_class(data=request.data).initial_data.get('id', None)

            # Add user ID to the response data
            if id is not None:
                response.data['id'] = id

            return response
        
class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class APILogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "All refresh tokens blacklisted"})
        refresh_token = self.request.data['refresh_token']
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "success"})
    