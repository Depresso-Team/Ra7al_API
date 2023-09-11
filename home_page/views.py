from django.shortcuts import render
from .models import SliderPhoto
from rest_framework import generics
from .serializers import SliderPhotoSerializer

# Create your views here.




# Slider View For Home Page
class SliderPhotoList(generics.ListAPIView):
    queryset = SliderPhoto.objects.all()
    serializer_class = SliderPhotoSerializer