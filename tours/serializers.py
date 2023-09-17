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




class HighestRateByStateSerializer(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()

    class Meta:
        model = ToursList
        fields = '__all__'  # Include all fields from the ToursList model
       

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




# Tours List
class ToursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursList
        fields = '__all__'



# Tours Reviews
class ReviewSerializer(serializers.ModelSerializer):
    reviewer_username = serializers.CharField(source='reviewer.username', read_only=True)

    class Meta:
        model = Reviews
        fields = ['id', 'reviewer_username', 'review', 'date']


# Create Review
class CreateReviewSerializer(serializers.Serializer):
    tour_id = serializers.IntegerField()
    review = serializers.CharField(max_length=500)



from rest_framework import serializers

class TourDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='reviews_set')

    class Meta:
        model = ToursList
        fields = ['id', 'name', 'description', 'price', 'state_id', 'company_name', 'duration', 'location', 'status', 'message', 'rate', 'saved', 'guide', 'photo', 'reviews']

