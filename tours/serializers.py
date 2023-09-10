from rest_framework import serializers
from .models import STATES, ToursList


# Tours List
class ToursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursList
        fields = ('id' , 'name', 'location', 'company_name','state_id', 'rate')
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
