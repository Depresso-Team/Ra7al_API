from rest_framework.generics import CreateAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import ToursList
from .serializers import ToursListSerializer
from rest_framework.views import APIView


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





# List all Tours
class ToursListView(APIView):
    def get(self, request, format=None):
        tours = ToursList.objects.all()
        serializer = ToursListSerializer(tours, many=True)

        response_data = {
            "status": True,
            "tours": serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)




# Tour Detail with put and delete
class ToursListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ToursList.objects.all()
    serializer_class = ToursListSerializer