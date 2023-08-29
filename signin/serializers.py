# Import necessary modules from Django REST framework
from rest_framework import serializers
from .models import User, Guide

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Serialize all fields of the User model

# Serializer for Guide model
class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'  # Serialize all fields of the Guide model
