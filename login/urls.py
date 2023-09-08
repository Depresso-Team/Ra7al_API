from django.urls import path, include
from .views import *


urlpatterns = [
    path('register/', register_user, name='register'),  # Endpoint for user registration
    path('register2/', RegisterUserView.as_view(), name='register-user'),  # Endpoint for user registration using a class-based view
    path('login/', user_login, name='login'),  # Endpoint for user login
    path('logout/', user_logout, name='logout'),  # Endpoint for user logout
    path('all_users', get_all_users, name='get_all_users'),  # Endpoint to get all users
    path('users/<int:user_id>/', user_detail, name='user-detail'),  # Endpoint for user detail view
    path('guides/', GuideList.as_view(), name='guide-list'),
]
