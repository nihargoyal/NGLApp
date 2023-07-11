from django.db.models import Sum
from django.http import Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from apis.models import App, UserTask
from apis.serializers import AppSerializer, UserTaskSerializer, UserProfileSerializer, UserSerializer
from apis.authentication import AdminJWTAuthentication, UserJWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .jwt_views import AdminTokenObtainPairView, UserTokenObtainPairView, TokenRefreshView
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
import json

@api_view(['POST'])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@authentication_classes([UserJWTAuthentication])
@permission_classes([IsAuthenticated])
def app_list(request):
    if request.method == 'GET':
        completed_apps = UserTask.objects.filter(user=request.user, completed=True).values_list('app_id', flat=True)
        apps = App.objects.exclude(id__in=completed_apps)
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([AdminJWTAuthentication])
@permission_classes([IsAdminUser])
def app_create(request):
    if request.method == 'POST':
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@authentication_classes([UserJWTAuthentication])
@permission_classes([IsAuthenticated])
def app_detail(request, pk):
    try:
        app = App.objects.get(pk=pk)
    except App.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = AppSerializer(app)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserTaskSerializer(data=request.data)
        if serializer.is_valid():

            completed_task = UserTask.objects.filter(user=request.user, app=app).first()
            if completed_task:
                return Response({'message': 'Task already completed by the user'}, status=400)

            user = request.user
            user_detail = UserTask.objects.get(user=user)
            user_detail.points += app.points
            user_detail.save()

            screenshot = request.FILES.get('screenshot')
            serializer.save(user=request.user, app=app, screenshot=screenshot, completed=True)

            return Response({'message': 'Task completed successfully'}, status=201)

        return Response(serializer.errors, status=400)



@api_view(['PUT', 'DELETE'])
@authentication_classes([AdminJWTAuthentication])
@permission_classes([IsAdminUser])
def app_update(request, pk):
    try:
        app = App.objects.get(pk=pk)
    except App.DoesNotExist:
        raise Http404

    if request.method == 'PUT':
        serializer = AppSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        app.delete()
        return Response(status=204)


@api_view(['GET'])
@authentication_classes([UserJWTAuthentication])
@permission_classes([IsAuthenticated])
def user_task_list(request):
    if request.method == 'GET':
        user_tasks = UserTask.objects.all()
        serializer = UserTaskSerializer(user_tasks, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@authentication_classes([AdminJWTAuthentication])
@permission_classes([IsAdminUser])
def user_task_detail(request, pk):
    try:
        user_task = UserTask.objects.get(pk=pk)
    except UserTask.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = UserTaskSerializer(user_task)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user_task.delete()
        return Response(status=204)


@api_view(['GET'])
@authentication_classes([UserJWTAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([UserJWTAuthentication])
@permission_classes([IsAuthenticated])
def total_points(request):
    user = request.user
    total_points = UserTask.objects.filter(user=user, completed=True).aggregate(Sum('app__points'))['app__points__sum']
    if not total_points:
        total_points = 0
    return Response({'total_points': total_points})


class LoginView(APIView):
    def post(self, request):
        body = request.body.decode('utf-8')
        data = json.loads(body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request=request, username=username, password=password)

        if user:
            login(request, user)
            if user.is_superuser:
                token_view = AdminTokenObtainPairView.as_view()
            else:
                token_view = UserTokenObtainPairView.as_view()

            # Generate tokens using the appropriate token view
            response = token_view(request._request)
            refresh_token = response.data['refresh']
            access_token = response.data['access']

            # Set refresh and access token cookies
            response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True, samesite='Strict')
            # response.data['refresh'] = 'Bearer ' + refresh_token
            # response.data['access'] = 'Bearer ' + access_token

            return response
        return Response({'error': 'Invalid credentials'}, status=401)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        response = Response()
        response.delete_cookie('refresh_token')
        response.data = {
            'message': 'Logout successful',
        }
        return response
