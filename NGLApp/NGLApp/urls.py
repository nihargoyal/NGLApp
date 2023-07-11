from django.contrib import admin
from django.urls import path
from apis.jwt_views import AdminTokenObtainPairView, UserTokenObtainPairView, TokenRefreshView
from apis.views import (
    user_registration,
    app_list,
    app_create,
    app_detail,
    app_update,
    user_task_list,
    user_task_detail,
    user_profile,
    total_points,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/admin/', AdminTokenObtainPairView.as_view(), name='admin_token_obtain_pair'),
    path('api/token/user/', UserTokenObtainPairView.as_view(), name='user_token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', user_registration, name='user-registration'),
    path('api/apps/list/', app_list, name='app-list'),
    path('api/apps/create/', app_create, name='app-create'),
    path('api/apps/detail/<int:pk>/', app_detail, name='app-detail'),
    path('api/apps/update/<int:pk>/', app_update, name='app-update'),
    path('api/tasks/list/', user_task_list, name='user-task-list'),
    path('api/tasks/detail/<int:pk>/', user_task_detail, name='user-task-detail'),
    path('api/profile/', user_profile, name='user-profile'),
    path('api/total-points/', total_points, name='total-points'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]