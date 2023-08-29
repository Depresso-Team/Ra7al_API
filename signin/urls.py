from django.urls import path , include
from. import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('users',views.UserRegistrationView)
router.register('guides',views.GuideRegistrationView)


urlpatterns = [
    path("tourrist/", include(router.urls)),
    path("guides/", include(router.urls)),
]