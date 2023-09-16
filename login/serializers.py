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
        fields = ['id', 'username','full_name' ,'email', 'password', 'phone', 'address', 'country_code', 'photo_url', 'languages', 'is_guide', 'session_message']
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



# Guide
class GuideSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    review = GuidesReviewsSerializer(many=True, read_only=True, source='guidesreviews_set')
    tour_list = serializers.SerializerMethodField()  # New field for tour details

    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'age', 'license', 'address', 'rate', 'review', 'tour_list']

    def get_tour_names(self, obj):
        # Get the tour names associated with the guide
        return list(obj.tourslist_set.values_list('name', flat=True))  # Assuming 'name' is the field in your Tour model

    def get_tour_list(self, obj):
        # Get the list of tour details (id, name, price, state_id, location, duration, photo) associated with the guide
        tour_queryset = obj.tourslist_set.all()
        tour_data = [
            {
                'id': tour.id,
                'name': tour.name,
                'price': tour.price,
                'state_id': tour.state_id,  
                'location': tour.location,  
                'duration': tour.duration,   
            }
            for tour in tour_queryset
        ]
        return tour_data

    rate = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )






# Best Guides
from rest_framework import serializers

class AddressField(serializers.CharField):
    def to_representation(self, obj):
        return obj.address

class HighestRatedGuideSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')
    address = AddressField(source='user', read_only=True)  # Add this field for address

    class Meta:
        model = Guide
        fields = ['id', 'username', 'personal_photo', 'rate', 'address']  # Include 'address' field


# Save a Guide by his ID
class SaveGuideSerializer(serializers.Serializer):
    guide_id = serializers.IntegerField()



# Saved Guides
class SavedGuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'




# Guide Detail
# class GuideSerializer(serializers.ModelSerializer):
#     username = serializers.ReadOnlyField(source='user.username')
#     languages = serializers.CharField(source='user.languages')
#     tour_ids = serializers.SerializerMethodField()

#     class Meta:
#         model = Guide
#         fields = ['personal_photo', 'username', 'age', 'address', 'license', 'rate', 'languages', 'Identity', 'tour_ids']

#     def get_tour_ids(self, obj):
#         # Assuming you have a reverse relationship 'guided_tours' from Guide to Tour
#         guided_tours = obj.user.guided_tours.all()
#         return [tour.id for tour in guided_tours]




class GuideListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    address = serializers.CharField(source='user.address')
    # Remove the source keyword argument for personal_photo
    personal_photo = serializers.ImageField()  # Remove 'source' here

    class Meta:
        model = Guide
        fields = ['id', 'username', 'address', 'personal_photo', 'rate','license','saved']




