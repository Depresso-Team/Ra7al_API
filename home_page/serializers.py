from rest_framework import serializers
from .models import SliderPhoto , Bannar





# Serializer Class For Home Page
class SliderPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderPhoto
        fields = '__all__'




class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bannar
        fields = ('id', 'title', 'bannar_url')

