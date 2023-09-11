from rest_framework import serializers
from .models import SliderPhoto





# Serializer Class For Home Page
class SliderPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderPhoto
        fields = '__all__'