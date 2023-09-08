from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'phone', 'address', 'country_code', 'photo_url', 'languages', 'is_guide', 'session_message']
        extra_kwargs = {'password': {'write_only': True}}  # Password is write-only in API

    def create(self, validated_data):
        # Create a new CustomUser instance using validated data
        user = CustomUser(**validated_data)

        # Set the password using the set_password method to ensure it's securely hashed
        user.set_password(validated_data['password'])

        # Save the user object to the database
        user.save()

        return user


from rest_framework import serializers
from .models import Guide

class GuideSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'background_URL']
