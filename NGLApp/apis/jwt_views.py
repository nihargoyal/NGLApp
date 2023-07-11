from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class AdminTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get('refresh')
        access = response.data.get('access')

        if refresh and access:
            response.set_cookie('refresh_token', refresh, httponly=True, secure=True, samesite='Strict')
            response.data = {
                'refresh': refresh,
                'access': access,
            }
        return response


class UserTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get('refresh')
        access = response.data.get('access')

        if refresh and access:
            response.set_cookie('refresh_token', refresh, httponly=True, secure=True, samesite='Strict')
            response.data = {
                'refresh': refresh,
                'access': access,
            }
        return response


class TokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get('refresh')
        access = response.data.get('access')

        if refresh and access:
            response.set_cookie('refresh_token', refresh, httponly=True, secure=True, samesite='Strict')
            response.data = {
                'refresh': refresh,
                'access': access,
            }
        return response
