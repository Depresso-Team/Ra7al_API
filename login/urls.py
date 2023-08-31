from django.urls import path
from .views import register_user, user_login, user_logout , get_all_users , user_detail , RegisterUserView




urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('all_users', get_all_users, name='get_all_users'),
    path('users/<int:user_id>/', user_detail, name='user-detail'),
    path('register2/', RegisterUserView.as_view(), name='register-user'),
]
