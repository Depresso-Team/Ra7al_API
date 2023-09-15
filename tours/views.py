from rest_framework.generics import CreateAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import ToursList, Reviews
from .serializers import SaveTourSerializer, SavedToursSerializer, ToursListSerializer, HighestRateByStateSerializer, CreateReviewSerializer
from rest_framework.views import APIView
from django.db.models import Max
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from login.models import Guide
from rest_framework import generics, status




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





# Best Tours
class HighestRateByState(APIView):
    def get(self, request):
        # Get the state with the highest rate for each state
        queryset = ToursList.objects.values('state_id').annotate(highest_rate=Max('rate')).order_by('-highest_rate')
        
        # Limit the queryset to the top 5 results
        queryset = queryset[:5]

        # Create a list to store the highest rate, location, name, company name, and duration for each state
        highest_rates_by_state = []

        for item in queryset:
            state_id = item['state_id']
            highest_rate = item['highest_rate']
            
            # Get the location, name, company name, and id with the highest rate for the current state
            highest_data = ToursList.objects.filter(state_id=state_id, rate=highest_rate).values('id', 'location', 'name', 'company_name', 'duration').first()
            
            # Add the state_id, highest_rate, highest_location, name, company_name, and id to the list
            highest_rates_by_state.append({
                'id': highest_data['id'] if highest_data else None,
                'state_id': state_id,
                'highest_rate': highest_rate,
                'highest_location': highest_data['location'] if highest_data else None,
                'name': highest_data['name'] if highest_data else None,
                'company_name': highest_data['company_name'] if highest_data else None,
                'duration': highest_data['duration'] if highest_data else None  # Include duration here
            })
        
        # Serialize the data using the HighestRateByStateSerializer
        serializer = HighestRateByStateSerializer(highest_rates_by_state, many=True)

        response_data = {
            "status": True,
            "message": "success",
            "tours": serializer.data
        }
        return Response(response_data)



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
                guide = Guide.objects.get(pk=guide_id)  # Replace 'Guide' with the actual model name
                serializer.validated_data['guide'] = guide
            except Guide.DoesNotExist:
                # Handle the case where the specified guide does not exist
                return Response({"status": False, "message": "Guide not found"}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)

        # Customize the response format
        response_data = {
            "status": True,
            "message": "created successfully",
            "tour": serializer.data
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)






class CreateReviewView(generics.CreateAPIView):
    serializer_class = CreateReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            tour_id = serializer.validated_data['tour_id']
            review_text = serializer.validated_data['review']

            try:
                tour = ToursList.objects.get(pk=tour_id)
                review = Reviews(tour=tour, review=review_text)
                review.save()
                return Response({'message': 'Review created successfully'}, status=status.HTTP_201_CREATED)
            except ToursList.DoesNotExist:
                return Response({'error': 'Tour not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
