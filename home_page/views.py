from django.shortcuts import render
from .models import SliderPhoto , Bannar
from rest_framework import generics
from .serializers import SliderPhotoSerializer , BannerSerializer

# Create your views here.




# Slider View For Home Page
class SliderPhotoList(generics.ListAPIView):
    queryset = SliderPhoto.objects.all()
    serializer_class = SliderPhotoSerializer



# Banner Create
class BannerListCreateView(generics.ListCreateAPIView):
    queryset = Bannar.objects.all()
    serializer_class = BannerSerializer



# Banner List
class BannerListView(generics.ListAPIView):
    queryset = Bannar.objects.all()
    serializer_class = BannerSerializer



# Banner Update , Delete
class BannerUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bannar.objects.all()
    serializer_class = BannerSerializer
