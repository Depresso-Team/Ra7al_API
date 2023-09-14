from rest_framework import serializers
from .models import STATES, ToursList , Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['review']


# Tours List
class ToursListSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True, read_only=True, source='reviews_set')  # Assuming related_name is 'reviews_set'

    class Meta:
        model = ToursList
        fields = ['name', 'description', 'price', 'location', 'rate', 'saved', 'reviews', 'guide']
        read_only_fields = ('status',)



# Best Tours
class HighestRateByStateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    company_name = serializers.CharField(max_length=100)
    state_name = serializers.SerializerMethodField()  
    highest_location = serializers.CharField(max_length=100, allow_null=True)
    highest_rate = serializers.FloatField()
    state_id = serializers.CharField(max_length=2)

    def get_state_name(self, obj):
        return dict(STATES).get(obj['state_id'])


# Save The Tour
class SaveTourSerializer(serializers.Serializer):
    tour_id = serializers.IntegerField()



# Saved Tours
class SavedToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursList
        fields = ['name','description', 'price', 'location', 'rate', 'saved']
