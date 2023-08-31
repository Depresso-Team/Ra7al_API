from django.urls import path
from .views import register_user, user_login, user_logout
from login import views



urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('all_users', views.get_all_users, name='get_all_users'),
    path('users/<int:user_id>/', views.user_detail, name='user-detail'),
]
