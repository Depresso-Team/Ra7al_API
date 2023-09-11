from django.urls import path

from .views import *



# Routes
urlpatterns = [
    path('',SliderPhotoList.as_view(),name='home')
]
