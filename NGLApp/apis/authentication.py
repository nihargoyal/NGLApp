from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class AdminJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            user = super().authenticate(request)
        except AuthenticationFailed:
            return None

        if user and user[0].is_superuser:
            return user

class UserJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            user = super().authenticate(request)
        except AuthenticationFailed:
            return None

        if user and not user[0].is_superuser:
            return user