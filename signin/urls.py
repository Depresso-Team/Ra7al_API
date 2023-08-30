# Import necessary modules from Django and Django REST framework
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a DefaultRouter instance for automatic URL routing
router = DefaultRouter()
router.register('users', views.UserRegistrationView)
router.register('guides', views.GuideRegistrationView)

# Define URL patterns for the application
urlpatterns = [
    # Include automatically generated URLs for 'users' and 'guides' resources under different endpoints
    path("tourist/", include(router.urls)),
    path("guides/", include(router.urls)),
    path('user/login/', views.UserLoginView.as_view(), name='user-login'),
    path('guide/login/', views.GuideLoginView.as_view(), name='guide-login'),
]
