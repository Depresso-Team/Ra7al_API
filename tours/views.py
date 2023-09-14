from rest_framework.generics import CreateAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import ToursList
from .serializers import SaveTourSerializer, SavedToursSerializer, ToursListSerializer, HighestRateByStateSerializer
from rest_framework.views import APIView
from django.db.models import Max
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from login.models import Guide




# Create a Tour
class ToursListCreateView(CreateAPIView):
    queryset = ToursList.objects.all()
    serializer_class = ToursListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Set the 'status' field to True before saving
        serializer.validated_data['status'] = True

        # Retrieve the guide ID from the request data (assuming it's provided in the request)
        guide_id = request.data.get('guide')

        if guide_id:
            try:
                guide = Guide.objects.get(pk=guide_id)
                serializer.validated_data['guide'] = guide
            except Guide.DoesNotExist:
                # Handle the case where the specified guide does not exist
                return Response({"status": False, "message": "Guide not found"}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)

        # Customize the response format
        response_data = {
            "status": True,
            "message": "created successfully",
            "tours": [serializer.data]
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
    pagination_class = CustomPageNumberPagination  





# Tour Detail with put and delete
class ToursListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ToursList.objects.all()
    serializer_class = ToursListSerializer




# Best Tours , filtered by rate 
class HighestRateByState(APIView):
    def get(self, request):
        # Get the state with the highest rate for each state
        queryset = ToursList.objects.values('state_id').annotate(highest_rate=Max('rate')).order_by('-highest_rate')
        
        # Limit the queryset to the top 5 results
        queryset = queryset[:5]

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
    

# =====================================================================

# Save The Tour
class SaveTourView(APIView):
    def post(self, request):
        serializer = SaveTourSerializer(data=request.data)
        if serializer.is_valid():
            tour_id = serializer.validated_data['tour_id']
            try:
                tour = ToursList.objects.get(pk=tour_id)
                tour.saved = True
                tour.save()
                return Response({'message': 'Tour saved successfully.'})
            except ToursList.DoesNotExist:
                return Response({'message': 'Tour not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Saved Tours List
class SavedToursListView(ListAPIView):
    queryset = ToursList.objects.filter(saved=True)  # Filter saved tours
    serializer_class = SavedToursSerializer
