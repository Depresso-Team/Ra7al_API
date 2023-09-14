from rest_framework import serializers
from .models import CustomUser , Guide , GuidesReviews
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from tours.models import ToursList



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



class GuidesReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidesReviews
        fields = ['review']


# Guides List
class GuideSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    review = GuidesReviewsSerializer(many=True, read_only=True, source='guidesreviews_set')
    tour_ids = serializers.SerializerMethodField()

    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'background_URL', 'rate', 'review', 'tour_ids']

    def get_tour_ids(self, obj):
        # Get the tour IDs associated with the guide
        return list(obj.tourslist_set.values_list('id', flat=True))

    rate = serializers.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )





# Best Guides
class HighestRatedGuideSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'background_URL', 'rate']



# Save a Guide by his ID
class SaveGuideSerializer(serializers.Serializer):
    guide_id = serializers.IntegerField()



# Saved Guides
class SavedGuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'
