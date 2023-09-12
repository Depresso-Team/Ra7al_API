from django.urls import path
from .views import *


# Routes
urlpatterns = [
    path('slider/',SliderPhotoList.as_view(),name='slider'),
    path('banner/', BannerListCreateView.as_view(), name='banner'),
    path('banner/all/', BannerListView.as_view(), name='banner-list'),
    path('banner/<int:pk>/', BannerUpdateDeleteView.as_view(), name='banner-update-delete'),
]
