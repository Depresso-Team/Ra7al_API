from rest_framework import serializers
from .models import  STATES,  ToursList , Reviews
from login.models import Guide


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['review']


# Tours List
class ToursListSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True, read_only=True, source='reviews_set')  # Assuming related_name is 'reviews_set'

    class Meta:
        model = ToursList
        fields = ['id', 'name', 'description', 'price', 'location', 'rate', 'saved', 'reviews','duration','location']
        read_only_fields = ('status',)





# Tours List
# class ToursListSerializer(serializers.ModelSerializer):
#     reviews = ReviewsSerializer(many=True, read_only=True, source='reviews_set')  # Assuming related_name is 'reviews_set'

#     class Meta:
#         model = ToursList
#         fields = ['id', 'name', 'description', 'price', 'location', 'rate', 'saved', 'reviews','duration','location']
#         read_only_fields = ('status',)






# class HighestRateByStateSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     company_name = serializers.CharField(max_length=100)
#     state_name = serializers.SerializerMethodField()
#     highest_location = serializers.CharField(max_length=100, allow_null=True)
#     highest_rate = serializers.FloatField()
#     state_id = serializers.CharField(max_length=2)
#     duration = serializers.IntegerField()  

#     def get_state_name(self, obj):
#         return dict(STATES).get(obj['state_id'])
















# serializers.py

from rest_framework import serializers

class HighestRateByStateSerializer(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()

    class Meta:
        model = ToursList
        fields = '__all__'  # Include all fields from the ToursList model
        # Add any additional fields you want to include here

    def get_state_name(self, obj):
        return dict(STATES).get(obj.state_id)








# Save The Tour
class SaveTourSerializer(serializers.Serializer):
    tour_id = serializers.IntegerField()



# Saved Tours
class SavedToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursList
        fields = ['name','description', 'price', 'location', 'rate', 'saved']





class ToursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursList
        fields = '__all__'




class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class CreateReviewSerializer(serializers.Serializer):
    tour_id = serializers.IntegerField()
    review = serializers.CharField(max_length=500)
