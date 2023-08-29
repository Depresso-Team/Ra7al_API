# Import necessary modules from Django REST framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Import models and serializers from application
from .models import User, Guide
from .serializers import UserSerializer, GuideSerializer



# User registration view using APIView
class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your logic for creating a new user
        class UserRegistrationView(viewsets.ModelViewSet):
              queryset = User.objects.all()
              serializer_class = UserSerializer

        # Assuming 'user' is the created user object
        message = User.session_message
        return Response({"message": message}, status=status.HTTP_201_CREATED)


# Guide registration view using APIView
class GuideCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your logic for creating a new guide
        class GuideRegistrationView(viewsets.ModelViewSet):
              queryset = Guide.objects.all()
              serializer_class = GuideSerializer

        # Assuming 'guide' is the created guide object
        message = Guide.session_message
        return Response({"message": message}, status=status.HTTP_201_CREATED)




# User registration viewset
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Guide registration viewset
class GuideRegistrationView(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer