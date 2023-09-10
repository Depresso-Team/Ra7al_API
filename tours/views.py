from rest_framework.generics import CreateAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import ToursList
from .serializers import ToursListSerializer, HighestRateByStateSerializer
from rest_framework.views import APIView
from django.db.models import Max
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView




# Create a Tour
class ToursListCreateView(CreateAPIView):
    queryset = ToursList.objects.all()
    serializer_class = ToursListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Set the 'status' field to True before saving
        serializer.validated_data['status'] = True
        self.perform_create(serializer)

        # Customize the response format
        response_data = {
            "status": True,
            "message": "created successfully",
            "tours": [
                {
                    "id": serializer.instance.id,
                    "name": serializer.instance.name,
                    "location": serializer.instance.location,
                    "company": serializer.instance.company_name,
                    "state_id": serializer.instance.state_id
                }
            ]
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


# Pagination Class
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 500


# List all Tours
class ToursListView(ListAPIView):
    queryset = ToursList.objects.all()
    serializer_class = ToursListSerializer
    pagination_class = CustomPageNumberPagination  # Use your custom pagination class





# Tour Detail with put and delete
class ToursListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ToursList.objects.all()
    serializer_class = ToursListSerializer




# Best Tours , filtered by rate 
class HighestRateByState(APIView):
    def get(self, request):
        # Get the state with the highest rate for each state
        queryset = ToursList.objects.values('state_id').annotate(highest_rate=Max('rate')).order_by('-highest_rate')
        
        # Create a dictionary to store the highest rate, location, and name for each state
        highest_rates_by_state = {}
        
        for item in queryset:
            state_id = item['state_id']
            highest_rate = item['highest_rate']
            
            # Get the location, name, and company name with the highest rate for the current state
            highest_data = ToursList.objects.filter(state_id=state_id, rate=highest_rate).values('location', 'name', 'company_name').first()
            
            # Add the state_id, highest_rate, highest_location, name, and company_name to the dictionary
            highest_rates_by_state[state_id] = {
                'state_id': state_id,
                'highest_rate': highest_rate,
                'highest_location': highest_data['location'] if highest_data else None,
                'name': highest_data['name'] if highest_data else None,
                'company_name': highest_data['company_name'] if highest_data else None
            }
        
        # Serialize the data using the HighestRateByStateSerializer
        serializer = HighestRateByStateSerializer(highest_rates_by_state.values(), many=True)

        response_data = {
            "status": True,
            "message": "success",
            "guides": serializer.data
        }

        return Response(response_data)

