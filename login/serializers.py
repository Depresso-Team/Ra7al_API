from rest_framework import serializers
from .models import CustomUser , Guide
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator



# User
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'phone', 'address', 'country_code', 'photo_url', 'languages', 'is_guide', 'session_message']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user





# Guides List
from rest_framework import serializers

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'background_URL']

    rate = serializers.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )



# from django.core.validators import MinValueValidator, MaxValueValidator


# Best Guides
class HighestRatedGuideSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'background_URL', 'rate']
