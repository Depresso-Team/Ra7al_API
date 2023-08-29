from django.urls import path , include
from. import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('viewset',views.UserRegistrationView)


urlpatterns = [
    path("viewsets/", include(router.urls)),
]