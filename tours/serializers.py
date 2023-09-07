from rest_framework import serializers
from .models import ToursList



class ToursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursList
        fields = ('id' , 'name', 'location', 'company_name','state_id')
        read_only_fields = ('status',)
