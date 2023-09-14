from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_user, name='register'),  # Endpoint for user registration
    path('register2/', RegisterUserView.as_view(), name='register-user'),  # Endpoint for user registration using a class-based view
    path('login/', user_login, name='login'),  # Endpoint for user login
    path('logout/', user_logout, name='logout'),  # Endpoint for user logout
    path('all_users', get_all_users, name='get_all_users'),  # Endpoint to get all users
    path('guides/', GuideList.as_view(), name='guide-list'), # All Guides
    path('highest_rated_guide/', HighestRatedGuide.as_view(), name='highest_rated_guide'), # Best Guides
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'), # Endpoint for user detail view
    path('save-guide/', SaveGuideView.as_view(), name='save-guide'),
    path('saved-guides/', SavedGuidesListView.as_view(), name='saved-guide-list'),
    path('guides/<int:pk>/', GuideDetailView.as_view(), name='guide-detail'),
]
